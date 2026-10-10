# ==============================================
#  STRING CONCEPTS IN PYTHON.
# ==============================================

# Strings are sequences of characters.
# They are enclosed within:
#   - single quotes (' ')
#   - double quotes (" ")
#   - triple quotes (''' ''' or """ """)
# Strings are immutable — once created, their content cannot be changed.

# -------------------------------------------------
# 0. Creation
# -------------------------------------------------
# Example 0.1
str1 = 'Hello'
str2 = "Nexus"
str3 = '''This is a multi-line string'''
num_to_str = str(341)  # Convert number to string

print("0. Creation Examples:")
print(str1)
print(str2)
print(str3)
print(num_to_str)
print()

# -------------------------------------------------
# 1. Indexing & Slicing
# -------------------------------------------------
# Example 1.1
a = "Noir Nation"
print("1. Indexing & Slicing:")
print(a[0], a[-1])      # First and last character
print(a[0:4])           # Slice from index 0 to 3
print(a[:6])            # Slice from start to index 5
print(a[3:])            # Slice from index 3 to end
print(a[::4])           # Step slicing
print(a[4::])           # From index 4 to end
print(a[::-1])          # Reverse string
print()

# -------------------------------------------------
# 2. String Operations
# -------------------------------------------------
s = "Noir"
v = "Nation"
print("2. Operations:")
print(s + " " + v)       # Concatenation
print("Na" * 3)          # Repetition
print("ir" in s)         # Membership check
print("Na" in v)
print("Na" in s)
print(len(s), len(v))    # Length
print()

# -------------------------------------------------
# 3. Escape Characters
# -------------------------------------------------
print("3. Escape Characters:")
print("Night\nTale")         # Newline
print("Noir\tNation")        # Tab
print("He said: \"Hello\"")  # Double quotes inside string
print("c:\\Users\\PythonNexus")  # Backslashes
print()

# -------------------------------------------------
# 4. String Methods
# -------------------------------------------------
w = "  Night Tale  "
print("4. Methods:")
print(w.strip())                    # Remove spaces
print(w.upper())                    # Uppercase
print("night Tale".capitalize())    # Capitalize first letter
print("hello-hello-hello".replace("hello", "hi", 2))  # Replace
print("Night Tale".count("i"))      # Count occurrences
print("Night Tale".find("le"))      # Find position
print("Noir456".isalnum())          # Check alphanumeric
print("Fairy Tale".title())         # Title case
print("report.pdf".endswith(".pdf"))# Endswith check
print()

# -------------------------------------------------
# 5. Splitting & Joining
# -------------------------------------------------
data = "apple,banana,mango"
parts = data.split(",")
print("5. Splitting & Joining:")
print(parts)
print(" | ".join(parts))     # Join with separator

lines = "a\nb\nm".splitlines()
awh = "a=b=m".split("=", 1)  # Split only once
print(lines)
print(awh)
print()

# -------------------------------------------------
# 6. Formatting
# -------------------------------------------------
name, score = "Abdullah", 93.653
print("6. Formatting:")

# 6.1 f-strings
print(f"{name} scored {score:.2f}%")  # Format with 2 decimals
print(f"{7 * 5 = }")                  # Inline expression

# 6.2 str.format()
print("Hello {}, You got {}%".format(name, round(score, 2)))

# 6.3 Old style (% operator)
print("Hello %s, You got %.2f%%" % (name, score))
print()

# -------------------------------------------------
# 7. Checking Content
# -------------------------------------------------
print("7. Checking Content:")
print("123".isdigit())          # Digits
print("Ⅻ".isdigit(), "Ⅻ".isnumeric())  # Roman numerals
print("abc".isalpha())          # Alphabets
print("123abc".isalnum())       # Alphanumeric
print("  ".isspace())           # Spaces only
print("Title Case".istitle())   # Title case check
print("lower".islower(), "UP".isupper())  # Lower & upper check
print()

# -------------------------------------------------
# 8. Raw String
# -------------------------------------------------
path = r"C:\new_folder\test.txt"
print("8. Raw String:")
print(path)
print()

# -------------------------------------------------
# 9. Translation & Reversing
# -------------------------------------------------
vowels = "aeiou"
table = str.maketrans("aeiou", "12345")   # Replace vowels with numbers
print("9. Translation & Reversing:")
print("Fairy Tale".translate(table))

# Delete characters by mapping them to None
delete_vowels = {ord(c): None for c in vowels}
print("Fairy Tale".translate(delete_vowels))  # Removes vowels

s = "banana"
print(s[::-1])                      # Reverse using slicing
print("".join(reversed(s)))         # Reverse using reversed()
print()

# -------------------------------------------------
# 10. Looping, Skipping, Breaking
# -------------------------------------------------
s = "Fairy Tale"
print("10. Looping, Skipping, Breaking:")

# 10.1 Looping through characters
for ch in s:
    print(ch, end=" ")
print()

# 10.2 Skipping 'a'
for ch in s:
    if ch == "a":
        continue
    print(ch, end=" ")
print()

# 10.3 Stop loop when 'i' is found
for ch in s:
    if ch == "i":
        print("Found:", ch)
        break

# 10.4 Else clause in for loop (runs if no break)
for ch in s:
    if ch == "i":
        break
else:
    print("No 'i' found")
