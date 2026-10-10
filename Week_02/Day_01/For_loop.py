# Loop through each character in a string
language = "python nexus"
for y in language:
    print(y)  # Prints each letter on a new line

# Loop using range(start, stop, step)
for i in range(3, 9, 2):
    print(i)  # Prints numbers: 3, 5, 7

# Multiplication table for a given number
num = int(input("Enter a number: "))
print("\n", str(num), "table:\n")
for i in range(1, 21):
    print(str(num), "x", str(i), "=", str(num * i))

# Print numbers and their squares
for num in range(1, 8):
    print("Number: ", num, "| Square:", num * num)

# Loop through a list of friends
friends = ["Ali", "Aleem", "Yaqoob", "Ibad"]
for friend in friends:
    print("Salam", friend)

# Print even numbers from 1 to 9
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# Loop through each letter in a word
word = 'pashtu'
for letter in word:
    print(letter)

# # Countdown from 5 to 1
for i in range(5, 0, -1):
    print(i)
print("Time's up!")

# # Find and print prime numbers from 1 to 49
for num in range(1, 50):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:  # If divisible, it's not prime
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")

# Pyramid star pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), "*" * (2 * i - 1))
