from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "calculator API is running"}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}