# -------------------------------
# Sets in Python
# -------------------------------
# Definition:
# A Set is an unordered, mutable (changeable), and unindexed collection of unique elements.
# It does not allow duplicate values and supports mathematical set operations like union, intersection, etc.

# -------------------------------
#  1. Creating Sets
# -------------------------------

# Set with elements
nums = {1, 2, 4}
print(nums)               # {1, 2, 4}
print(type(nums))         # <class 'set'>

# Empty set (must use set(), {} creates a dictionary)
num = set()
print(num)                # set()
print(type(num))          # <class 'set'>

# Duplicate values are automatically removed
numbers = {1, 2, 3, 4, 3, 4}
print(numbers)            # {1, 2, 3, 4}
print(type(numbers))      # <class 'set'>

# Creating set from a list
my_set = set([1, 2, 4, 3, 2, 34, 23])
print(my_set)             # {1, 2, 34, 3, 4, 23}
print(type(my_set))       # <class 'set'>


# -------------------------------
# 2. Set Operations
# -------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union → {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection → {3, 4}
print(A - B)   # Difference → {1, 2}
print(B - A)   # Difference → {5, 6}
print(A ^ B)   # Symmetric Difference → {1, 2, 5, 6}


# -------------------------------
# 3. Add & Remove Elements
# -------------------------------
nums = {1, 34, 23, 21}

nums.add(4)        # Add single element
print(nums)

nums.remove(1)     # Remove element (error if not present)
print(nums)

nums.update([5, 8])  # Add multiple elements
print(nums)

nums.discard(5)    # Remove element (no error if not present)
print(nums)

nums.pop()         # Removes random element
print(nums)

nums.clear()       # Remove all elements
print(nums)        # set()


# -------------------------------
#  4. Iterating Through a Set
# -------------------------------
colors = {"yellow", "blue", "white", "olive"}
for color in colors:
    print(color)   # Prints each element (order not fixed)


# -------------------------------
# 5. Built-in Functions on Sets
# -------------------------------
numbers = {10, 20, 30, 40}

print(len(numbers))    # Number of items → 4
print(max(numbers))    # Maximum → 40
print(min(numbers))    # Minimum → 10
print(sum(numbers))    # Sum → 100


# -------------------------------
# 6. Frozen Set (Immutable Set)
# -------------------------------
# Frozenset → same as set but cannot be modified
f_set = frozenset([1, 2, 3, 4])
print(f_set)           # frozenset({1, 2, 3, 4})
# f_set.add(5)  Error: cannot add to frozenset
