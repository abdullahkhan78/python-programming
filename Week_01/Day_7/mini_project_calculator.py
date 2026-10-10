# Function definitions

# This function adds two numbers
def add(num1, num2):
    return num1 + num2

# This function subtracts the second number from the first
def sub(num1, num2):
    return num1 - num2

# This function multiplies two numbers
def mul(num1, num2):
    return num1 * num2

# This function divides the first number by the second
# It checks for division by zero
def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

# This function returns the remainder (modulus)
# It also checks for division by zero
def mod(num1, num2):
    if num2 != 0:
        return num1 % num2
    else:
        return "Cannot modulo by zero"

# Taking input from the user

# Input: First number (converted to float for decimal support)
num1 = float(input("Enter first number: "))

# Input: Operation symbol (+, -, *, /, %)
op = input("Enter an operation (+, -, *, /, %): ")

# Input: Second number
num2 = float(input("Enter second number: "))

# Performing operation based on user's input

# Check which operation was entered, then call the correct function
if op == "+":
    print("Result:", add(num1, num2))
elif op == "-":
    print("Result:", sub(num1, num2))
elif op == "*":
    print("Result:", mul(num1, num2))
elif op == "/":
    print("Result:", div(num1, num2))
elif op == "%":
    print("Result:", mod(num1, num2))
else:
    # If user enters something else, show an error
    print("Invalid operation!")
