import logging
from utils.validator import validate_expression
from utils.calculator import calculate
LOG_FILE = "logs/app.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")
def main():
    while True:
        expression = input("Enter a mathematical expression (or type 'exit' to quit): ").strip()
        if expression.lower() == 'exit':
            print("Goodbye!")
            break
        if validate_expression(expression):
            result = calculate(expression)
            logging.info(f"Expression: {expression} | Result: {result}")
            print(f"Result: {result}")
        else:
            print("Invalid expression! Please enter a valid mathematical expression.")
if __name__ == "__main__":
    main()
