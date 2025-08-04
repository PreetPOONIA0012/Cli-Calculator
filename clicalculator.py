# Cli-Calculatt using Python. This tool allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division through a terminal interface.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Welcome to the CLI Calculator!")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operator!"

            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the program
calculator()