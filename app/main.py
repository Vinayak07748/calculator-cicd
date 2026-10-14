from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "calculator API is running"}

@app.get('/multiply')
def multiply(a: float, b: float):
    return {"a": a, "b": b, "result": a * b}