# ============================================================
# Python Loops
# ============================================================
# Loops are used to repeat a block of code multiple times.
# Types of Loops:
#   1. for loop   → Iterates over a sequence (range, list, string, etc.)
#   2. while loop → Repeats until a condition is False
# ============================================================


# ============================================================
# 1. Printing Numbers 1 to 10 using for loop
# ============================================================
for num in range(1, 11):
    print(num)


# ============================================================
# 2. Multiplication Table of 5
# ============================================================
num = 5
print("Table of", num, ":\n")
for i in range(1, 21):
    print(num, "X", i, "=", num * i)


# ============================================================
# 3. Sum of First n Natural Numbers (using loop)
# ============================================================
n = int(input("Enter a number: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("The sum of first", n, "natural numbers is:", sum_n)


# ============================================================
# 4. Sum of First n Natural Numbers (using formula)
# Formula: n(n + 1) / 2
# ============================================================
n = int(input("Enter a number: "))
sum_n = n * (n + 1) // 2
print("The sum of first", n, "natural numbers is:", sum_n)


# ============================================================
# 5. Printing Even Numbers from 1 to 50 (using while loop)
# ============================================================
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1


# ============================================================
# 6. Prime Number Checker
# ============================================================
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):   # check divisors up to sqrt(n)
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


# ============================================================
# 7. Pyramid Pattern using while loop
# ============================================================
rows = 8
i = 1
while i <= rows:
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces, "*" * stars)  # Spaces then stars
    i += 1
