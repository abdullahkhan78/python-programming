# input function in python
# The input() function is an essential feature in Python that allows taking input from the user.
# (*) It always reads the input as a string and returns it.

#========================#
# Example 1: Greeting

name = input("Enter your name: ")                  # Ask for user's name
print("Hello!", name)                              # Greet the user

age = input("Enter your age: ")                    # Ask for user's age
print("You are", age, "years old")                 # Display age
print("Next year you will be", {int(age)+1})       # Show age after one year (converted to int)

#========================#

# Example 2: Adding Two Numbers

num2 = input("Enter the second number: ")          # Get second number (as string)

print("The sum of", num1, "and", num2, "is", sum)  # Print the result

num1 = input("Enter the first number: ")           # Get first number (as string)


#========================#


# Example 3: BMI Calculator
 # Taking user input
name = input("Enter your name: ")
age = input("Enter your age: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# BMI formula
bmi = weight / (height ** 2)

# Printing basic info
print("\nName:", name)
print("Age:", age)
print("BMI:", round(bmi, 2))

# Checking BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight")
elif 25<= bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
                      # Display BMI rounded to 2 decimal places



#========================#


# Example 4: Area of a Rectangle

length = float(input("Enter the length: "))          # Ask for rectangle length
width = float(input("Enter the width: "))            # Ask for rectangle width

area = length * width                                # Calculate area (length × width)

print("The area of the rectangle is:", area)         # Print the area
