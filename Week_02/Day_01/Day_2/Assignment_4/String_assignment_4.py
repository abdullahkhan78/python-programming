# ========================================
#String Practice Questions
# ========================================

# ----------------------------------------
# Question 1:
# Limit the decimal places to 2 digits using format method
# ----------------------------------------

pi = 3.14159265359
print(pi)   # Original value of pi

print(round(pi, 2))   # Using round() → 2 decimal places (3.14)
print("The value of pi is  {:.2f}".format(pi))  # Using format method

# ----------------------------------------
# Question 2:
# Extract characters from index 2 to 8 with a step of 2
# Given: my_string = "python course"
# ----------------------------------------

my_string = "python course"
print(my_string[2:8:2])   # Start=2, Stop=8, Step=2 → "to "

# ----------------------------------------
# Question 3:
# Slice to get only the middle character(s)
# For even length → 2 middle characters
# For odd length → 1 middle character
# ----------------------------------------

my_string1 = "python"   # Length=6 (even)
# middle chars → "th"

my_string2 = "pythons"  # Length=7 (odd)
# middle char → "h"

def mid_str(word):
    middle = int(len(word)/2)       # Find middle index
    if len(word) % 2 == 0:          # Even length string
        return word[middle-1 : middle+1]
    else:                           # Odd length string
        return word[middle]

print(mid_str(my_string2))   # Output: "h"

# ----------------------------------------
# Question 4:
# Remove the first 3 and last 3 characters
# Given: my_string = "Regression Analysis"
# ----------------------------------------

my_string = "Regression Analysis"
print(my_string[3:-3])   # Remove first 3 and last 3 → "ression Anal"

# ----------------------------------------
# Extra Example: Reverse a string
# ----------------------------------------

name = "Nexus"
print(name)         # Nexus
print(name[::-1])   # Reverse string → suxeN

# ----------------------------------------
# Palindrome Check
# Palindrome = string which reads same forward & backward
# e.g. "madam", "level", "racecar"
# ----------------------------------------

name  = "madam"

def is_palindrome(s):
    if s == s[::-1]:   # Compare string with its reverse
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is NOT a palindrome")

print(is_palindrome(name))   # Output: "madam is a palindrome"
