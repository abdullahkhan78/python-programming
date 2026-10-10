# Basic print statement
print("Hello, Python")

# Taking input from user and greeting
name = input("Enter name: ")   # user enters their name
print("Hello,", name)          # output greeting with name

# Swapping two numbers using a temporary variable
a = 5
b = 6

temp = a   # store value of a in temp
a = b      # assign b’s value to a
b = temp   # assign temp’s (old a) value to b

print("After swapping:") 
print("a =", a)   # now a has b’s value
print("b =", b)   # now b has a’s value

# Taking two numbers as input and performing arithmetic operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add = a + b           # addition
diff = a - b          # subtraction
prod = a * b          # multiplication

print("Sum is:", add)
print("Difference is:", diff)
print("Multiplication is:", prod)

# Program to check even/odd without using if-else
num = int(input("Enter a number: "))

# Method 1: Using shorthand if-else (ternary operator)
print("Even" if num % 2 == 0 else "Odd")

# Method 2: Using list indexing
print(["Even", "Odd"][num % 2])

# Method 3: Using dictionary mapping
print({0: "Even", 1: "Odd"}[num % 2])
