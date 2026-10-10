# ============================================================
# Python Functions
# ============================================================
# A function is a block of reusable code that performs a specific task.
# - Defined using `def` keyword
# - Can take inputs (parameters)
# - Can return output (using `return`)
# - Makes code reusable and organized
# ============================================================


# ============================================================
# 1. Function to Add Two Numbers
# ============================================================
# def add(num1, num2):       # function with two parameters
#     return num1 + num2     # returns sum

# print(add(4, 5))           # Output: 9


# # ============================================================
# # 2. Function to Find Square of a Number
# # ============================================================
# def square(num):
#     return num * num       # returns square

# print(square(9))           # Output: 81


# # ============================================================
# # 3. Function with User Input
# # ============================================================
# def square2(num):
#     return num * num

# n = int(input("Enter a number: "))
# print("Square of", n, "is =", square2(n))


# # ============================================================
# # 4. Palindrome Checker Function
# # ============================================================
# def is_palindrome(s):
#     if s == s[::-1]:       # check if string equals its reverse
#         return f"{s} is a palindrome."
#     else:
#         return f"{s} is not a palindrome."

# name = "madam"
# print(is_palindrome(name)) # Output: madam is a palindrome.


# # ============================================================
# # 5. Function with Default Parameter
# # ============================================================
# def greet(name="Guest"):          # default value is "Guest"
#     return f"Hello, {name}!"

# print(greet())                    # Output: Hello, Guest!
# print(greet("Abdullah"))          # Output: Hello, Abdullah!




# def add_num(*args):
#     return sum(args)

# print(add_num(1,2,3))
# print(add_num(10, 23))


num = [1,3,4,5,6]
result = map(lambda n: n * n, num)
print(list(result))



