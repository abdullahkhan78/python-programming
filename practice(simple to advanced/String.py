# =====================================
# STRING PROGRAMS REVISION
# =====================================

# 1. Reverse a string
# Definition: Reversing means printing the string from end to start.
name = "python"
print("Reversed string:", name[::-1])   # [::-1] slices the string in reverse


# 2. Count vowels in a string
# Definition: A vowel is any of 'a, e, i, o, u'. We count how many are in the text.
text = "python programming"
vowels = "aeiou"
count = 0

for char in text.lower():        # convert to lowercase to handle both cases
    if char in vowels:           # check if character is a vowel
        count += 1
print("Number of vowels:", count)


# 3. Check if a string is palindrome
# Definition: A palindrome is a word that reads the same forward and backward.
name = "madam"
if name == name[::-1]:           # compare string with its reverse
    print("Palindrome")
else:
    print("Not a palindrome") 


# 4. Replace all spaces in a string with '-'
# Definition: Replace() is used to substitute characters in a string.
text = "i am learning python"
new_text = text.replace(" ", "-")    # replace spaces with '-'
print("After replacing spaces:", new_text)


# 5. Find the most repeated word in a sentence
# Definition: We split sentence into words, count frequency, then find max.
line = "python is easy and python is powerful and python is fun"
words = line.split()        # split into list of words
freq = {}

for word in words:                             # loop through each word
    freq[word] = freq.get(word, 0) + 1         # count frequency

most_repeated = max(freq, key=freq.get)        # find word with highest count
print("Most repeated word is:", most_repeated)
print("Frequency:", freq[most_repeated])


# 6. Extract all digits from a string
# Definition: Digits are numeric characters (0–9). We check with isdigit().
text = "ab354cf34"
digits = []

for ch in text:
    if ch.isdigit():          # check if character is a digit
        digits.append(int(ch))    # convert string digit → integer

print("Extracted digits:", digits)
