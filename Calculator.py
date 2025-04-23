# Simple calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Input from the user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Chose operation (+, -, *, /): ")

result = None

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    if num2 != 0:
        result = divide(num1, num2)
    else:
        result = "Error: Division by zero!"

if isinstance(result, (int, float)):
    print("Result:", result)
else:
    print(result if result else "Invalid operation!")