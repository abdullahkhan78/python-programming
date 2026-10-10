# # ======================== #
# #      Conditional Statements
# # ======================== #

# # if, elif, and else are used for decision making in Python.

# # --------------------------- #
# # Topics to be covered:
# # --------------------------- #
# # 1. Definition
# # 2. Types of conditional statements
# # 3. Examples

# # ======================== #
# #      Definition:
# # ======================== #
# # Conditional statements allow you to execute specific blocks of code
# # based on whether a condition is True or False.
# # They help control the flow of a program.

# # ======================== #
# #      if statement:
# # ======================== #

# # The "if" statement executes a block only if the condition is True.

# # Example 1
# # num1 = 34
# # num2 = 23

# # if num1 > num2:
# #     print("Num1 is greater")  # This line runs because 34 > 23

# # Example 2
# age = int(input("Enter your age: "))  # Ask user for age
# if age > 19:
#     print("You are an adult!")  # Executes only if age is greater than 19


# # ======================== #
# #      if-else statement:
# # ======================== #

# # if-else runs one block if condition is True, another if False.

# temperature = 30

# if temperature > 25:
#     print("It's a hot day.")  # This line runs because 30 > 25
# else:
#     print("It's a cool day.")  # This would run if temperature <= 25

# # Example 2
# age1 = int(input("Enter your age: "))  # Ask for age

# if age1 > 18:
#     print("You are an adult.")  # If condition is true
# else:
#     print("You are not an adult.")  # If condition is false


# ======================== #
#      if-elif-else statement:
# ======================== #

# This structure checks multiple conditions one by one.

# Example 1: Traffic light simulation
# signal = input("Enter the signal color: ")  # Ask for traffic signal color

# if signal == "Red":
#     print("Stop")
# elif signal == "Yellow":
#     print("Get Ready")
# elif signal == "Green":
#     print("Go")
# else:
#     print("Invalid Signal!")  # If color doesn't match any option

# Example 2: Days of the week
day = input("Enter a number (1-7): ")  # Input from user

if day == "1":
    print("Monday")
elif day == "2":
    print("Tuesday")
elif day == "3":
    print("Wednesday")
elif day == "4":
    print("Thursday")
elif day == "5":
    print("Friday")
elif day == "6":
    print("Saturday")
elif day == "7":
    print("Sunday")
else:
    print("Invalid day!")  # If input is not 1-7

# # Example 3: Number classification
# num = int(input("Enter a number: "))  # Input number from user

# if num < 0:
#     print("Negative number")  # If less than 0
# elif num == 0:
#     print("Zero")  # If exactly 0
# elif 1 <= num <= 10:
#     print("Between 1 and 10")  # If between 1 and 10
# elif 11 <= num <= 20:
#     print("Between 11 and 20")  # If between 11 and 20
# else:
#     print("Greater than 20")  # If greater than 20


# # ======================== #
# #      Nested if-else:
# # ======================== #

# # Example: Check if a number is positive and also check if it's even or odd

# num = int(input("Enter a number: "))  # Ask user to enter a number

# if num > 0:
#     print("Positive number")  # First level check: number is positive

#     # Nested condition to check if it's even or odd
#     if num % 2 == 0:
#         print("Even number")  # Runs if number is divisible by 2
#     else:
#         print("Odd number")   # Runs if not divisible by 2
# else:
#     print("Not a positive number")  # If number is 0 or negative


# # ======================== #
# #      Conditional Expression (Ternary Operator):
# # ======================== #

# # Example: Check if age is adult or minor using one-line if-else

# age = int(input("Enter your age: "))  # Get age from user

# # Conditional expression to assign result in one line
# status = "Adult" if age >= 18 else "Minor"

# print(status)  # Output the result
