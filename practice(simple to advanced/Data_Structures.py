# =====================================
# Python Revision Notes (Lists, Tuples, Sets, Dictionaries)
# =====================================

# --------------------------
# LISTS
# --------------------------

# A list is an ordered, mutable (changeable) collection in Python.
# Syntax: list_name = [elements]

fruits = ["Mango", "Apple", "Pinepple", "Orange", "Banana"]
print(fruits[1])   # Access element by index -> Output: Apple

# Add new element at the end of list
fruits.append("Cherry")
print(fruits)


# Remove duplicates from a list
fruits = ["Mango", "Apple","Mango", "Pinepple", "Orange", "Banana"]

# Method 1: Using set (but it does not preserve order)
# uniqe_fruits = list(set(fruits))

# Method 2: Using loop (preserves order)
uniqe_fruits = []
for fruit in fruits:
    if fruit not in uniqe_fruits:
        uniqe_fruits.append(fruit)
print(uniqe_fruits)   


# Find largest number in a list
number = [12, 34, 45, 54, 42, 76, 54]
largest = max(number)
print(largest)


# Flatten a nested list
number = [[1, 2], [3, 4]]
flat = []
for sublist in number:
    for num in sublist:
        flat.append(num)
print(flat)


# Sort list of tuples by second element
data = [(1, 3), (2, 1), (4, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)   # Output: [(2, 1), (4, 2), (1, 3)]


# --------------------------
# TUPLES
# --------------------------

# Tuples are immutable (unchangeable) ordered collections.
numbers = (1, 2, 3)
print(numbers)
print(type(numbers))
print(numbers[2])   # Access element by index


# Convert tuple into list (to modify it)
my_tuple = (1, 5, 7, 3, "Apple")
my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))


# Find max and min in tuple
nums = (34, 42, 632, 543, 131, 412)
print(max(nums))
print(min(nums))


# Count frequency of each element in a tuple
numbers = (23, 32, 45, 54, 23, 234, 653, 234, 645, 644)
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)


# --------------------------
# SETS
# --------------------------

# Sets are unordered collections with unique elements.
my_set = {1, 23, 234, 52, 53}
print(my_set)
print(type(my_set))


# Add and remove elements in set
my_set.add(30)
print(my_set)
my_set.remove(234)
print(my_set)


# Find common elements (intersection)
set1 = {1, 2, 3, 5}
set2 = {4, 5, 2, 5}
set3 = set1.intersection(set2)
print(set3)


# Find difference between sets
print(set1.difference(set2))  # Elements in set1 but not in set2
print(set2.difference(set1))  # Elements in set2 but not in set1


# Check if sets are disjoint (no common elements)
set1 = {1, 2, 3, 5}
set2 = {4, 6, 7, 8}
print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))


# Set comprehension: squares of even numbers from 1 to 10
squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(squares)


# --------------------------
# DICTIONARIES
# --------------------------

# Dictionaries store data as key-value pairs.
person = {"name": "Abdullah", "age": 20}
print(person)
print(type(person))


# Update value
person = {"name": "Abdullah", "age": 19}
person["age"] = 20
print(person)
print(person["name"])   # Access value using key
print(person["age"])


# Add new key-value pair
person = {"name": "Abdullah", "age": 19}
person["course"] = "python"
print(person)


# Merge two dictionaries
student = {"name": "Ahmad", "age": 21}
crs = {"course": "python"}

# Method 1: update()
student.update(crs)
print(student)

# Method 2: unpacking operator
my_dict = {**student, **crs}
print(my_dict)


# Dictionary comprehension: create dictionary of squares
list1 = [1, 2, 3]
squares = {num: num**2 for num in list1}
print(squares)   # Output: {1: 1, 2: 4, 3: 9}
