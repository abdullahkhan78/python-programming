# Dictionary -> Key-Value pair data structure in Python


# Example_1

my_dictionary = {'name': 'Abdullah', 'age': 20,'city': 'bannu'}  # creates a dictionary
print(my_dictionary)          # prints the dictionary
print(type(my_dictionary))    # prints the type (dict)


# Dictionary storing information about Abdullah(me)

student = {
    "name": "Abdullah",
    "age" : 20,
    "study": 11,
    "is_student": True
}
print(student)    # Prints the whole dictionary
print(student["name"])    # Access value of key 'name'
print(student["age"])      # Access value of key 'age'
print(student.get("age"))  # Safer way to access key
print(student["is_student"]) # Access value of key 'is_student'

# common dict operators

student["course"] = "python"    # Adding new key-value
print(student)

student.pop("age")              # Removing a key-value
print(student)

del student["course"]           # another way  to deleting a key-value
print(student)


if "name" in student:            # Checking if key exist
    print("Yes, name exists")


