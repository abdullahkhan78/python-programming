# ==============================
# Tuple in Python
# ==============================

# Definition:
# A tuple is a collection in Python that is:
# 1. Ordered → Elements have a fixed position.
# 2. Immutable → Once created, elements cannot be changed.
# 3. Allows Duplicates → Can contain repeated values.
# Tuples are useful for storing related but unchangeable data.

# ==============================
# Creating Tuples
# ==============================

# Simple tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

# Tuple with mixed data types
my_tuple1 = (1, "Nexus", 3.14, True)
print("Mixed Tuple:", my_tuple1)

# Tuple without parentheses
tuple1 = 1, 2, 3, 4, 5
print("Tuple without ():", tuple1)

# Using tuple() constructor
tuple2 = tuple((1, 2, 3, 4))
print("Tuple from constructor:", tuple2)

# Converting list to tuple
list1 = [1, 3, 5]
new_tuple = tuple(list1)
print("Tuple from list:", new_tuple)

# Creating single-element tuple (must add comma)
single_tuple = ("single",)
print("Single-element tuple:", single_tuple)


# ==============================
# Accessing Tuples: Indexing & Slicing
# ==============================
fruits = ('Mango', 'Cherry', 'Apple')
print("First fruit:", fruits[0])    # Indexing
print("Last fruit:", fruits[-1])    # Negative indexing

tuple4 = (43, 54, 3, 2, 5, 3, 2)
print("Sliced tuple (step 2):", tuple4[0:8:2])
print("Sliced tuple (step 3):", tuple4[0::3])


# ==============================
# Iterating over a Tuple
# ==============================
fruits = ("Pineapple", "Melon", "Apple")

print("Iteration using for loop:")
for fruit in fruits:
    print(fruit)

print("Iteration using while loop:")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# ==============================
# Tuple Operations
# ==============================
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd', 'e')

# Concatenation
tuple3 = tuple1 + tuple2
print("Concatenated Tuple:", tuple3)

# Repetition
tuplee = ("red", "blue", "yellow") * 2
print("Repeated Tuple:", tuplee)

# Membership
print("Is 'blue' in tuple?:", "blue" in tuplee)

# Length
print("Length of tuple:", len(tuplee))


# ==============================
# Tuple Functions
# ==============================
color = ('white', 'black', 'maroon', 'olive')
print("Count of 'black':", color.count('black'))
print("Index of 'olive':", color.index('olive'))

nums = (2, 4, 5, 6, 7)
print("Length:", len(nums))
print("Sum:", sum(nums))
print("Minimum:", min(nums))
print("Maximum:", max(nums))
print("Sorted List:", sorted(nums))   # returns list
print("Sorted Tuple:", tuple(sorted(nums)))


# ==============================
# Packing and Unpacking Tuples
# ==============================
a = "Abdullah"
b = 20
c = "Python"

tuple_pack = a, b, c
print("Packed Tuple:", tuple_pack)

name, age, course = tuple_pack  # Unpacking
print("Unpacked Values:", name, age, course)


# ==============================
# Modifying Tuples (Indirectly)
# ==============================
# Tuples are immutable, but we can:
# 1. Convert tuple → list
# 2. Modify list
# 3. Convert back list → tuple

tuple_nums = (23, 32, 54, 43, 23)
print("Original Tuple:", tuple_nums)

# Convert tuple to list
list_nums = list(tuple_nums)
print("Converted to List:", list_nums)

# Modify the list
list_nums[1] = 34
print("List after modification:", list_nums)

# Convert back to tuple
tuple_nums = tuple(list_nums)
print("Modified Tuple:", tuple_nums)
