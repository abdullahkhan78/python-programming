# ============================
# Python Conditional Statements
# ============================
# Definition:
# Conditional statements allow decision making in Python.
# Python uses: if, elif, else
# - if → checks first condition
# - elif → checks next condition if previous is false
# - else → runs if none of above conditions are true
# ============================


# ==============================================
# 1Check if a number is Positive, Negative or Zero
# ==============================================
x = int(input("Enter a number: "))

if x > 0:
    print("The number is positive.")
elif x == 0:
    print("The number is Zero.")
elif x < 0:
    print("The number is negative.")
else:
    print("Please input number!")


# ==============================================
# 2 Check if a number is Even or Odd
# ==============================================
e = int(input("Enter a number: "))

if e % 2 == 0:
    print("Even")
else:
    print("Odd")


# ==============================================
# 3 Find the Largest Number Among Three
# ==============================================
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("Num1 is the largest and equal to", num1)
elif num2 > num1 and num2 > num3:
    print("Num2 is the largest and equal to", num2)
else:
    print("Num3 is the largest and equal to", num3)

# Using built-in function
largest = max(num1, num2, num3)
print("The largest number is:", largest)


# ==============================================
# 4 Grade Calculator
# ==============================================
marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
elif 0 <= marks < 60:
    print("Grade F")
else:
    print("Invalid Marks")


# ==============================================
# 5 Greeting Based on Time
# ==============================================
# Method 1: Using float format (e.g. 13.30 for 1:30 PM)
time = float(input("Enter a time in (24-hour format): "))

if 5 <= time <= 11.59:
    print("Good Morning!")
elif 12 <= time <= 19.59:
    print("Good Afternoon!")
elif 20 <= time <= 23.59 or 0 <= time < 5:
    print("Good Night!")
else:
    print("Enter a valid time!")


# Method 2: Using proper HH:MM format
time = input("Enter a time in HH:MM (24-hour format): ")
hour, minute = map(int, time.split(':'))

if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 20:
    print("Good Afternoon!")
elif 20 <= hour <= 23 or 0 <= hour < 5:
    print("Good Night!")
else:
    print("Enter a valid time!")
