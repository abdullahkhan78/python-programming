#  Dictionary in Python
# Dictionary is a collection of key–value pairs.
# Keys must be unique and immutable, values can be of any type.
# Dictionaries are mutable (we can add, update, delete items).

# Creating an empty dictionary
my_dict  = {}
print(my_dict)   # {}

# Creating dictionary with curly braces {}
student = {"Name": "Abdullah", "Age":  20, "Course": 'python'}
print(student)   # {'Name': 'Abdullah', 'Age': 20, 'Course': 'python'}
print(type(student))  # <class 'dict'>

# Creating dictionary using dict() function
person = dict(name = "gullkhuban", age = 34, city = "lahore")
print(person)   # {'name': 'gullkhuban', 'age': 34, 'city': 'lahore'}
print(type(person))  # <class 'dict'>

# Creating dictionary from list of tuples
pairs = dict([("a", 1), ("b", 2), ("C", 3)])
print(pairs)   # {'a': 1, 'b': 2, 'C': 3}
print(type(pairs))  # <class 'dict'>


# Accessing Dictionary items
student = {"name": "Abdullah", "age": 20, "marks": 93}
print(student["name"])             # Direct access → Abdullah
print(student.get("marks"))        # Using get() → 93
print(student.get("grade", "not found"))  # If key not present → "not found"

# Note: get() is safer than direct access, avoids KeyError.


# Modifying Dictionary (add/update items)
student = {"name": "Ali", "marks": 88}

student["marks"] = 95      # Update existing value
student["grade"] = "A"     # Add new key–value pair

print(student)   # {'name': 'Ali', 'marks': 95, 'grade': 'A'}


# Removing items from Dictionary
student = {"name": "Ali", "age": 21, "marks": 88, "course": "Python"}

student.pop("age")      # Removes key 'age'
student.popitem()       # Removes the last inserted key–value
del student["marks"]    # Deletes 'marks' key
student.clear()         # Clears all items from dictionary


# Iterating through Dictionary
user = {"name": "Zara", "age": 23, "city": "Karachi"}

# Loop through keys
for key in user:
    print(key)    # name, age, city

# Loop through values
for value in user.values():
    print(value)  # Zara, 23, Karachi

# Loop through both keys and values
for key, value in user.items():
    print(key, ":", value)  
    # name : Zara
    # age : 23
    # city : Karachi


# Built-in Dictionary functions and methods
data = {"a": 1, "b": 2, "c": 3}

print(len(data))       # 3 → Number of items
print(data.keys())     # dict_keys(['a', 'b', 'c'])
print(data.values())   # dict_values([1, 2, 3])
print(data.items())    # dict_items([('a', 1), ('b', 2), ('c', 3)])

copy_data = data.copy()   # Creates a shallow copy of dictionary


# Nested Dictionary (dictionary inside dictionary)
students = {
    "std1": {"name": "Ali", "age": 22},
    "std2": {"name": "Sara", "age": 20}
}

print(students["std1"]["name"])   # Access nested value → Ali

# Note: Dictionaries can hold other dictionaries as values.
