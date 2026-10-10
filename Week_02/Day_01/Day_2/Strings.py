# A string is a sequence of characters.In python , strings are enclosed within the single('), double(""), or in a triple(""") quotation marks.

# Strings are immutable.ie once created , their character can't be changed.
# Syntax:
        # print('Hello! Nexus')

        # print("Won't give up!")

        # print(''' "Quotes" and 'single quotes' can be tricky.''')

        # Formated string::
        # A formated string in a python is a way to insert variables or expressions inside a string. It allows you to format the out put in readable and controlled way.

        # There are multiple ways to format strings in python.
        # 1. Old-style formating (% operator)
        # 2. str.format()method.
        # 3.  f-strings (formatted string literals).




# Srings simple examples.


str1 = 'Hello, Nexus!'
str2 = "Won't give up"
str3 = '''This is a multi-line string'''

print(str1)
print(str2)
print(str3)




# 1-> Old style formating(%):
# example.
name = "Abdullah"
age = 20
print("My name is %s and am %d years old."%(name, age))


name = "Abdullah"
age = 20
print("My name is {0} and am {1} years old.".format(name, age))
print(f"my name is {name} and am {age} years old.")
print(f" My age after 5 years will be {age + 5} years.")