# pf = int(input("Enter pf marks: "))
# ds = int(input("Enter ds marks: "))
# oop = int(input("Enter oop marks: "))

# average = (pf + ds + oop) / 3

# if average >= 90:
#     grade = "A"
# elif average >= 80:
#     grade = "B"
# elif average >= 70:
#     grade = "C"
# elif average >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("\n-----Student Report -----")
# print("pf:",pf)
# print("ds:", ds)
# print("oop:", oop)   
# print("Average:",round(average, 2))
# print("Grade:", grade) 





# def calculate_average(marks):
#     return sum(marks) / len(marks)

# def get_grade(average):
#     if average >= 90:
#         return "A"
#     elif average >= 80:
#         return "B"
#     elif average >= 70:
#         return "C"
#     elif average >= 60:
#         return "D"
#     else:
#         return "F"

# Student = {}

# while True:
#     name = input("Enter student name (or type 'stop' to finish):")
#     if name.lower() == "stop":
#         break

#     marks = []
#     for subject in ["Programmin fundamentals", "Descrete structures", "Operating system"]:
#         score = int(input(f"Enter marks for {subject}: "))
#         marks.append(score)

#     average = calculate_average(marks)
#     grade = get_grade(average)  
#     Student[name] = {"marks": marks, "average": average, "grade": grade}

#     print("\n------ Student Report ------")
# for name, details in Student.items():
#     print(f"Student: {name}")
#     print(f"Marks: {details['marks']}")
#     print(f"Average: {details['average']:.2f}")
#     print(f"Grade: {details['grade']}")
#     print("---------------------------")      