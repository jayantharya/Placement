from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from collections import deque, defaultdict
from db_connection import connect_db
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
db = connect_db()

if db is None:
    raise RuntimeError("Failed to connect to the database. Please check your .env file and MongoDB URI.")
app = FastAPI(title="PESCE BANK")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class Account(BaseModel):
    account_no: str
    name: str
    balance: float = 0.0

class Transaction(BaseModel):
    amount: float
    target_account: Optional[str] = None


# 1. Quick Sort (Sorting transactions by amount)
def quick_sort_transactions(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]['amount']
    left = [x for x in arr if x['amount'] > pivot]  # Descending order
    middle = [x for x in arr if x['amount'] == pivot]
    right = [x for x in arr if x['amount'] < pivot]
    return quick_sort_transactions(left) + middle + quick_sort_transactions(right)

# 2. BFS 
def bfs_transaction_path(start_acc: str, end_acc: str) -> bool:
    transfers = list(db.transactions.find({"type": "transfer"}, {"_id": 0}))
    
    
    graph = defaultdict(list)
    for t in transfers:
        graph[t['from_account']].append(t['to_account'])
        
    queue = deque([start_acc])
    visited = set([start_acc])
    
    while queue:
        current = queue.popleft()
        if current == end_acc:
            return True # Path found
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False 


@app.post("/accounts/", summary="CRUD: Create Account")
def create_account(acc: Account):
    if db.accounts.find_one({"account_no": acc.account_no}):
        raise HTTPException(status_code=400, detail="Account already exists")
    db.accounts.insert_one(acc.dict())
    return {"message": "Account created successfully", "account_no": acc.account_no}

@app.get("/accounts/{account_no}", summary="CRUD: Read Account")
def get_account(account_no: str):
    acc = db.accounts.find_one({"account_no": account_no}, {"_id": 0})
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc

@app.delete("/accounts/{account_no}", summary="CRUD: Delete Account")
def delete_account(account_no: str):
    result = db.accounts.delete_one({"account_no": account_no})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": "Account deleted successfully"}

@app.post("/accounts/{account_no}/deposit")
def deposit(account_no: str, tx: Transaction):
    db.accounts.update_one({"account_no": account_no}, {"$inc": {"balance": tx.amount}})
    db.transactions.insert_one({
        "account_no": account_no,
        "type": "deposit",
        "amount": tx.amount,
        "date": datetime.now()
    })
    return {"message": f"₹{tx.amount} deposited successfully."}

@app.post("/accounts/{account_no}/withdraw")
def withdraw(account_no: str, tx: Transaction):
    acc = db.accounts.find_one({"account_no": account_no})
    if not acc or acc['balance'] < tx.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds or account not found")
    
    db.accounts.update_one({"account_no": account_no}, {"$inc": {"balance": -tx.amount}})
    db.transactions.insert_one({
        "account_no": account_no,
        "type": "withdraw",
        "amount": tx.amount,
        "date": datetime.now()
    })
    return {"message": f"₹{tx.amount} withdrawn successfully."}

@app.post("/accounts/{account_no}/transfer")
def transfer(account_no: str, tx: Transaction):
    sender = db.accounts.find_one({"account_no": account_no})
    receiver = db.accounts.find_one({"account_no": tx.target_account})
    
    if not sender or not receiver:
        raise HTTPException(status_code=404, detail="Sender or receiver account not found")
    if sender['balance'] < tx.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
        
    db.accounts.update_one({"account_no": account_no}, {"$inc": {"balance": -tx.amount}})
    db.accounts.update_one({"account_no": tx.target_account}, {"$inc": {"balance": tx.amount}})
    
    db.transactions.insert_one({
        "from_account": account_no,
        "to_account": tx.target_account,
        "type": "transfer",
        "amount": tx.amount,
        "date": datetime.now()
    })
    return {"message": f"₹{tx.amount} transferred successfully."}

@app.get("/accounts/{account_no}/transactions", summary="Uses Quick Sort")
def get_sorted_transactions(account_no: str):
    # Fetch all transactions for the user
    txs = list(db.transactions.find({"$or": [{"account_no": account_no}, {"from_account": account_no}, {"to_account": account_no}]}, {"_id": 0}))
    # Apply Quick Sort
    sorted_txs = quick_sort_transactions(txs)
    return {"transactions": sorted_txs}

@app.get("/network/{acc1}/{acc2}", summary="Uses BFS")
def check_network(acc1: str, acc2: str):
    is_linked = bfs_transaction_path(acc1, acc2)
    return {"linked": is_linked, "message": "Transaction link found!" if is_linked else "No transaction link exists."}

app.mount(
    "/static",StaticFiles(directory="static"),
    name="static"
)

# Home Page
@app.get("/")
async def home():
    return FileResponse("static/index.html")