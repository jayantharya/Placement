from fastapi import FastAPI
app = FastAPI()
current_balance = 1000
@app.get("/")
def Bank():
    return {"message": "Welcome to the Bank"}
def Balance():
    global current_balance
    return {"balance": current_balance}
@app.get("/balance")
def get_balance():
    return Balance()
def Deposit(amount):
    global current_balance
    current_balance += amount
    return {"balance": current_balance}
@app.post("/deposit")
def deposit(amount: int):
    return Deposit(amount)
def Withdraw(amount):
    global current_balance
    current_balance -= amount
    return {"balance": current_balance}
@app.post("/withdraw")
def withdraw(amount: int):
    return Withdraw(amount)
def Transfer(amount):
    global current_balance
    current_balance -= amount
    return {"balance": current_balance}
@app.post("/transfer")
def transfer(amount: int):
    return Transfer(amount)
def browser():
    import webbrowser
    webbrowser.open("http://localhost:8000") 
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)