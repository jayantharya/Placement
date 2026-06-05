from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def Bank():
    return {"message":"Welcome to the Bank"}
def Balance():
    return {"balance":1000}
@app.get("/balance")
def get_balance():
    return Balance()
def Deposit(amount):
    return {"balance":1000+amount}
@app.post("/deposit")
def deposit(amount:int):
    return Deposit(amount)
def Withdraw(amount):
    return {"balance":1000-amount}
@app.post("/withdraw")
def withdraw(amount:int):
    return Withdraw(amount)
def Transfer(amount):
    return {"balance":1000-amount}
@app.post("/transfer")
def transfer(amount:int):
    return Transfer(amount)
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)  
def browser():
    import webbrowser
    webbrowser.open("http://localhost:8000")