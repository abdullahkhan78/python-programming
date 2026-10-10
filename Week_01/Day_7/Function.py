# Function in Python
# A function is a block of code that performs a specific task.
# You can use it whenever you want by calling its name.
# This avoids repeating the same code and improves readability and reusability.

# Basic Concepts
# Create function: Use the "def" keyword to define a function.
# Call function: Use the function's name followed by () to run it.
# Parameter: Variable listed inside parentheses in function definition.
# Argument: Actual value passed to the function when calling it.


# Example 1: Function without parameters
def Greeting():
    print("Hello Python Nexus")
Greeting()


# Example 2: Function with parameters
def add2nums(a, b):
    result = a + b
    print(result)
add2nums(4, 7)    


# Celsius to Fahrenheit converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_f = celsius_to_fahrenheit(25)
print(temp_f)  # Output: 77.0


# Built-in Functions (Already provided by Python)
print("Hello")
print("Abdullah")
print(max(4, 6))    # Returns the maximum
print(type(13.6))   # Returns the data type


# User-defined Function (You create it yourself)
def greet():
    print("Hello, Nexus")
greet()


# Example 1: Simple welcome message
def welcome_message():
    print("I am Abdullah.")
    print("I want to become a Python expert.")
welcome_message()


# Function with Parameters
def greet(name):
    print("Hello", name)
greet("Abdullah")  


# Example: Full name printer
def full_name(first, last):
    print("Your full name is:", first, last)
full_name("Abdullah", "Khan")    


# Function with Return Value
def add(a, b):
    return a + b

result = add(4, 7)
print(result)  # Output: 11


# Example: Square function
def square(num):
    return num * num

result = square(9)
print(result)  # Output: 81


# Default Parameter (Used when no argument is passed)
def greet(name="Friend"):
    print("Hello", name)

greet()              # Output: Hello Friend
greet("Abdullah")    # Output: Hello Abdullah


# Keyword Arguments (You can pass arguments in any order by naming them)
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Abdullah")    


# Variable-length Arguments

# *args → Accepts multiple positional arguments
def total(*numbers):
    print(sum(numbers))  # Adds all the numbers

total(4, 5, 4, 2)  # Output: 15
