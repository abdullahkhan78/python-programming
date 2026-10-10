# ============================================================
# Python Operators
# ============================================================
# Operators are special symbols used to perform operations.
# Types we are covering here:
#   1. Arithmetic Operators (+, -, *, /, %, //, **)
#   2. Comparison Operators (==, !=, >, <, >=, <=)
#   3. Logical Operators (and, or, not)
#   4. Identity Operators (is, is not)
#   5. Membership Operators (in, not in)
# ============================================================


# ============================================================
# 1. Arithmetic Operators
# Example: Finding area of rectangle
# ============================================================
length = 30
width = 10
area = length * width
print("Area =", area)   # Multiplication (*)


# Example: Modulus (remainder after division)
a = 29
b = 5
result = a % b
print("29 % 5 =", result)


# ============================================================
# 2. Logical Operators
# Check divisibility by both 3 and 5
# ============================================================
a = int(input("Enter a number: "))

if a % 3 == 0 and a % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# ============================================================
# 3. Comparison vs Identity Operators
# ============================================================
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # True → values are equal (comparison)
print(x is y)   # False → not same object in memory (identity)


# ============================================================
# 4. Membership Operators
# ============================================================
s = "python nexus"

if "python" in s:
    print("Yes, 'python' is present in string")
else:
    print("Not found")
