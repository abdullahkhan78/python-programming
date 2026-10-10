# Example 1: Simple while loop
count = 0
while count < 10:
    print(count)  # Prints numbers from 0 to 9
    count += 1
else:
    print("while loop ended")  # Runs when while loop ends naturally

# Password check loop
password = ''
while password != "abd123":  # Keep asking until correct password
    password = input("Enter password: ")
print("Access granted")

# Pyramid pattern using while loop
rows = 8
i = 1
while i <= rows:
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces, "*" * stars)  # Spaces then stars
    i += 1

# Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Sum of numbers from 1 to 5
i = 1
total = 0
while i <= 5:
    total = total + i
    i += 1
    print(total)  # Prints total after each addition

# Multiplication table using while loop
num = int(input('Enter a number: '))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
