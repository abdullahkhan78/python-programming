# Question - 01:
# Write a program to input student name and marks of three(3) subjects.
# Print name and percentage in output.

# Taking user input
student_name = input("Enter a student name: ")
pf_marks = int(input("Enter the PF marks: "))       # PF subject marks
ict_marks = int(input("Enter the ICT marks: "))     # ICT subject marks
mvc_marks = int(input("Enter the MVC marks: "))     # MVC subject marks

# Calculating percentage out of 300 total marks
percentage = ((pf_marks + ict_marks + mvc_marks) / 300) * 100

# Printing the result with percentage
print("The result of", student_name, "is", int(percentage), "%")



# Question - 02:
# Write a program that collects multiple data types to store in a dictionary and print the output.

# Creating an empty dictionary to store user information
