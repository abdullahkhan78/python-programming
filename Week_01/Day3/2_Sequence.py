# Sequence types in Python

# Sequence types store multiple items in an ordered way.pythhon has saveral built-in sequence types.
# 1-> String  (str)
# 2-> List    (list)
# 3-> Tuple  (tuple)
# 4-> Range  (range)

#----------------------------(#)----------------------------------

                   # String Examples

#example_1

s = "Abdullah"        # s is a string
s1 = "22"             # s1 is a string (even though it looks like a number)

print(s)              # prints the value of s
print(type(s))        # prints the type of s (string)

# Example_2

name = "abdullah"
print(name)
print(name[3])
print(len(name))


#--------------------------------#-------------------------------------#


                   # List data type Exmples


# Example_1

l = [1,2,4,2,56,'Nexus']        # l is a list with integers and a string
print(l)                        # prints the list
print(type(l))                  # prints the type of l (list)

# Example_2

fruits = ["Banana", "Mango", "Apple", "Orange"] 
print(fruits)                     # print all the four friuts names
print(fruits[2])                  # prints Apple (which is at index 2)
print(len(fruits))                # total length = 4
fruits.append("Strawberry")       # adding a new item (Strawberry)
print(fruits)                     # again print all items
print(len(fruits))                # again print the total length (5)



 #===================# Tuple data type Examples #=================#

# Tuple is like a list but it's immutable (can't be changed)

# Example_1

t = (6,5,3,78,5,4, "pynative")  # t is a tuple containing integers and a string
print(t)                        # prints the tuple
print(type(t))                  # prints the type of t (tuple)

# Example_2
colours = ("maroon", "black", "blue")
print(colours)
print(colours[1])
print(colours[2])
#colours.append("white")     # this will give an error bcz tuple is unchangeble


#====================# Range #===================#

# -> Range generates sequence of a numbers.

#Example_1

nums = range(5)
print(list(nums))
print(nums[3])

# Example_2 -> with start and end

even_numbers = range(2, 10, 2)    # (start(2), stop(10), step(2))
print(list(even_numbers))     # Output: [2, 4, 6, 8]







