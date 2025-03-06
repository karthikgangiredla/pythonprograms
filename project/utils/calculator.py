
def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return float(result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        return f"Error: {e}"