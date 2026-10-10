# Boolean data type in Python
# Can only have two values: True or False

bool1 = True            # bool1 is assigned the boolean value True
print(bool1)            # prints the value of bool1
print(type(bool1))      # prints the type (bool)

bool2 = False           # bool2 is assigned the boolean value False
print(bool2)            # prints the value of bool2
print(type(bool2))      # prints the type (bool)



# Example_2

is_student = True
has_laptop = True
likes_python = True

print(is_student)
print(has_laptop)
print(likes_python)


# Exampple_3

age = 20
zero_value = 0

print(bool(age))         # Output: True (non-zero number)
print(bool(zero_value))  # Output: False


# Example_4
name = "Abdullah"
empty_name = ""

print(bool(name))        # Output: True (not empty)
print(bool(empty_name))  # Output: False (empty string)
