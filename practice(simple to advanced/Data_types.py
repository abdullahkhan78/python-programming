# ============================================================
# 📘 Python Data Types & Type Casting
# ============================================================
# Definition:
# Data types represent the type of value a variable holds.
# Common types: int, float, str, bool
# Type casting means converting one data type into another.
# ============================================================


# ============================================================
# 1  Checking Types of Different Values
# ============================================================
a = "123"         # string type
print(type(a))    # <class 'str'>

b = 123           # integer type
print(type(b))    # <class 'int'>

c = 12.3          # float type
print(type(c))    # <class 'float'>

d = int(3.14)     # casting float → int
print(d)          # output: 3
print(type(d))    # <class 'int'>


# ============================================================
# 2 Type Casting with Input
# ============================================================
age = input("Enter age: ")   # input always returns string
print(age)                   # prints entered value as string
age2 = int(age)              # cast string → integer
print(type(age2))            # <class 'int'>


# ============================================================
# 3 Celsius → Fahrenheit Conversion
# ============================================================
celsius = float(input("Enter temperature in Celsius: "))  # input → float
fahrenheit = (9 / 5 * celsius) + 32
print("Temperature in Fahrenheit:", fahrenheit)


# ============================================================
# 4 Convert String Digits into List of Integers
# ============================================================
num = "1234"                 # string
num2 = list(map(int, num))   # map each character → int, then list
print(num2)                  # output: [1, 2, 3, 4]
