import math  # Import the math module for advanced mathematical functions

# Define basic arithmetic operations
def add(x, y): 
    return x + y  # Addition

def subtract(x, y): 
    return x - y  # Subtraction

def multiply(x, y): 
    return x * y  # Multiplication

def divide(x, y): 
    return x / y  # Division

def sqrt(x): 
    return math.sqrt(x)  # Square root

def exp(x, y): 
    return x ** y  # Exponentiation

# Ask the user to choose an operation
operation = input("Choose operation (+, -, *, /, sqrt, ^): ")

try:
    if operation == 'sqrt':
        # If the operation is square root, only one number is needed
        num = float(input("Enter number for square root: "))
        if num < 0:
            # Handle square root of negative number
            print("Error: Cannot take square root of a negative number.")
        else:
            print("Result:", sqrt(num))  # Display square root result
    else:
        # For other operations, get two numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform operation based on user input
        if operation == '+':
            print("Result:", add(num1, num2))  # Addition
        elif operation == '-':
            print("Result:", subtract(num1, num2))  # Subtraction
        elif operation == '*':
            print("Result:", multiply(num1, num2))  # Multiplication
        elif operation == '/':
            if num2 != 0:
                print("Result:", divide(num1, num2))  # Division
            else:
                print("Error: Division by zero!")  # Error for dividing by zero
        elif operation == '^':
            print("Result:", exp(num1, num2))  # Exponentiation
        else:
            print("Error: Invalid operation.")  # Handle invalid operations

except ValueError:
    # Handle invalid numeric input (e.g., if the user enters letters instead of numbers)
    print("Error: Invalid input. Please enter numeric values.")