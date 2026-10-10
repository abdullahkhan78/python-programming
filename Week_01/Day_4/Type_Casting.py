# Type Casting refers to the process of converting a value from one data type to another.

# Topics to be covered:
# a. Definition
# b. Examples
# c. Implicit Casting 
# d. Explicit Casting

# (*) Python has several built-in functions for type casting such as int(), float(), str(), bool()

#===================# int & str #=============#

a = 2
print(type(a))  # Output: <class 'int'> → 'a' is an integer

b = "1"
print(type(b))  # Output: <class 'str'> → 'b' is a string

# print(a + b)  #  Error: Cannot add int and str directly

c = int(b)       # Converts string '1' to integer
print(type(c))   # Output: <class 'int'>

print(a + c)     # Output: 3 → int + int works


#===================# str() Example #=============#

# Example: Convert int to string

mynum = 23
mynum2 = str(mynum)       # Converts integer 23 to string '23'
print(type(mynum2))       # Output: <class 'str'>


#===================# float to int #=============#

# Example: Convert float to int (decimal part will be removed)
f1 = 23.78
f2 = int(f1)              # Converts 23.78 to 23
print(type(f2))           # Output: <class 'int'>
print(f2)                 # Output: 23

#===================# Implicit Type Casting #=============#

# Python automatically converts int to float during arithmetic
var1 = 20                 # int
var2 = 10.5               # float
var3 = var1 + var2        # int + float → float
print(var3)               # Output: 30.5
print(type(var3))         # Output: <class 'float'>

#===================# Explicit Type Casting #=============#

# Manually converting int to string
int_num = 203
str_num = str(int_num)    # Converts 203 (int) to "203" (str)
print(type(str_num))      # Output: <class 'str'>

#===================# bool() Casting #=============#

# Convert integer to boolean
a1 = bool(1)              # Non-zero integers are True
print(a1)                 # Output: True
print(type(a1))           # Output: <class 'bool'>
