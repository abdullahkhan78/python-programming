# Sets data type in Python
# Sets are unordered collections of unique elements

# Exampl_1

my_sets = {2, 32, 43, 65, 44, 'mongosh'}  # defines a set with integers and a string
print(my_sets)          # prints the set
print(type(my_sets))    # prints the type (set)


# Example_2

numbers = {1,2,3,4,5,6,2,1,3}       
print(numbers)                   # Output: {1, 2, 3, 4} — duplicates removed


# Example_3
# add and remove items

fruits = {"Banana", "Mango"}
print(fruits)

fruits.add("Apple")        # add itme(Apple)
print(fruits)


fruits.remove("Mango")     # remove item(Mango)
print(fruits)



# Example_3

set1 = {1, 4, 5}        
set2 = {2, 1, 3}        
print(set1.union(set2))     # print all elements ,remove the  common
print(set1.intersection(set2))  # Prints only common  elements
print(set1.difference(set2))    # print  the  elements prresent  in  set1  but  not in  set2
print(set2.difference(set1))    # print the elements present  in  set2 but  not  in set1