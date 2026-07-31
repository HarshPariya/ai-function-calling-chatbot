from datetime import datetime


def calculator(a: float, b: float, operation: str):
    operation = operation.lower()

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    return "Invalid operation"


def get_current_time():
    return datetime.now().strftime("%I:%M %p")