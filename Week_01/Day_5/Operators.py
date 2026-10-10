# Arithmetic Operators
a = 10
b = 3

add = a + b         # Addition
sub = a - b         # Subtraction
mul = a * b         # Multiplication
div = a / b         # Division (float)
floor_div = a // b  # Floor Division
mod = a % b         # Modulus (remainder)
exp = a ** b        # Exponent (10^3)

# Assignment Operators
x = 5
x += 2    # x = x + 2 → x = 7
x *= 3    # x = x * 3 → x = 21
x -= 1    # x = x - 1 → x = 20

# Comparison Operators
is_equal = (a == b)
is_not_equal = (a != b)
is_greater = (a > b)
is_less = (a < b)
is_greater_equal = (a >= b)
is_less_equal = (a <= b)

# Logical Operators
cond1 = a > 5
cond2 = b < 5
logical_and = cond1 and cond2     # True if both are True
logical_or = cond1 or cond2       # True if any one is True
logical_not = not cond1           # Inverts the condition

# Output All
print("Arithmetic:")
print("Add:", add, "Sub:", sub, "Mul:", mul, "Div:", div)
print("Floor Div:", floor_div, "Mod:", mod, "Exp:", exp)

print("\nAssignment:")
print("Final value of x:", x)

print("\nComparison:")
print("Equal?", is_equal, "| Not Equal?", is_not_equal)
print("Greater?", is_greater, "| Less?", is_less)

print("\nLogical:")
print("AND:", logical_and, "| OR:", logical_or, "| NOT:", logical_not)
