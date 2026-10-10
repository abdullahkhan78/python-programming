# Student Report Card Generator.

name = input("Enter student name: ")
roll_no = input("Enter a student roll number: ")

pf = float(input("Enter pf marks:"))
ds = float(input("Enter ds marks:"))
dld = float(input("Enter dld marks:"))

total = pf + ds + dld

percentage = total / 3


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"  


status = "Pass" if percentage >= 50 else "Fail"

print("\n======= * Student Report Card * ======= ")
print("Name: ", name)
print("Roll No: ", roll_no)
print("Total: ", total)
print("percentage: ", percentage)
print("Grade: ", grade)
print("Status:", status)

