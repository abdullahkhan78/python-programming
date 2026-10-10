# ===========================
# Q1: Leap Year Checker
# ===========================

# Ask the user to enter a year
# year = int(input("Enter a year: "))

# Check if the year is a leap year
# Rule:
# - Divisible by 4 → leap year
# - Except if divisible by 100 → not a leap year
# - Unless it is also divisible by 400 → leap year
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")



# ===========================
# Q2: Login Authentication
# ===========================

# Predefined correct credentials
# predefined_username = 'Abdullah'
# predefined_password = 'abd123'

# # Input from user
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# # First check if username is correct
# if username == predefined_username:
#     # Now check if password is correct
#     if password == predefined_password:
#         print("Login successful!")
#     else:
#         print("Incorrect password!")
# else:
#     print("Invalid username!")



# ===========================
# Q3: Admission Eligibility
# ===========================

print("Enter PCM marks out of 100")

# Take marks input from user
physics_marks = int(input("Enter physics marks: "))
chemistry_marks = int(input("Enter chemistry marks: "))
maths_marks = int(input("Enter maths marks: "))

#Check eligibility based on two conditions:
#Condition 1:
- Maths >= 65
- Physics >= 55
- Chemistry >= 50
# Total of all 3 subjects >= 180
OR
#Condition 2:
- Physics + Maths >= 140

if (maths_marks >= 65 and
    physics_marks >= 55 and
    chemistry_marks >= 50 and
    (maths_marks + physics_marks + chemistry_marks) >= 180) or \
   (maths_marks + physics_marks) >= 140:
    print("You are eligible")
else:
    print("You are not eligible!")
