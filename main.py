from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from calculator_logic import add, subtract, multiply, divide

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Calculator is running!"}


# Calculator

ops = {"+": add, "-": subtract, "*": multiply, "/": divide}


@app.get("/calculate")
def calculate(num1: float, num2: float, operation: str):
    if operation not in ops:
        return {"error": "Invalid operation"}
    return {"result": ops[operation](num1, num2)}
