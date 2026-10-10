# ========================================
# Lists in Python
# ========================================

# What is a List?
# A list in Python is a collection of items (elements) that are:
#  - Ordered (sequence maintained)
#  - Mutable (can be changed)
#  - Allow duplicates
# Lists are one of the most versatile data structures in Python.

# ========================================
# Creating Lists
# ========================================
my_list = ["Apple", 3.14, 1, True]   # List with different data types
print(my_list)                       # Prints the list
print(type(my_list))                 # <class 'list'>

# ========================================
# Accessing and Modifying Lists
# ========================================
fruits = ['Apple', 'Banana', 'Mango'] 
print(fruits)                        # Prints original list
fruits[1] = "Cherry"                 # Modifying element at index 1
print(fruits)                        # ['Apple', 'Cherry', 'Mango']

# ========================================
# List Operations
# ========================================
numbers = [10, 20, 30]
print(len(numbers))                  # Length of list → 3
print(numbers + [40, 50])            # Concatenation → [10,20,30,40,50]
print(numbers * 2)                   # Repetition → [10,20,30,10,20,30]
print(30 in numbers)                 # Membership test → True

# ========================================
# List Methods
# ========================================
fruits = ['Banana', 'Mango', 'Cherry']
print(fruits)

fruits.append("Mango")               # Add at the end
print(fruits)

fruits.insert(1,"Orange")            # Insert at index 1
print(fruits)

fruits.remove("Banana")              # Remove element by value
print(fruits)

fruits.pop()                         # Remove last element
print(fruits)

fruits.sort()                        # Sort list in ascending order
print(fruits)

fruits.reverse()                     # Reverse the list
print(fruits)

# ========================================
# Slicing in Lists
# ========================================
nums = [1, 2, 3, 4, 5]
print(nums)

print(nums[1:4])     # Slice from index 1 to 3 → [2,3,4]
print(nums[1::])     # Slice from index 1 to end → [2,3,4,5]
print(nums[1:-1])    # From index 1 to second last → [2,3,4]
print(nums[0:-1])    # From start to second last → [1,2,3,4]
print(nums[:3])      # First 3 elements → [1,2,3]
print(nums[::4])     # Step of 4 → [1,5]

# ========================================
#  Nested Lists
# ========================================
nested = [[1, 2], [3, 4], [5, 6]]
print(nested)

print(nested[0][1])  # Accessing inner list → element 2

# ========================================
# Iterating in Lists
# ========================================
for fruit in ["Apple", "Banana", "Mango"]:
    print(fruit)  # Loop through each element and print

# ========================================
# List Comprehension
# ========================================
# Shortcut way to create lists in one line
squares = [x**2 for x in range(5)]   # Generate squares of 0 to 4
print(squares)                       # [0, 1, 4, 9, 16]
