# Basic Data types in python

# (1) -> Numeric  

a1 = 2    # a1 is an integer value
a2 = 4.5  # a2 is a float value

print(type(a1))   # prints the type of a1 (int)
print(type(a2))   # prints the type of a2 (float)
print(a1 + a2)    # prints the result of adding a1 and a2 (int + float)

#---INT EXAMPLES---
age = 20     # current age
print("Abdullah's age:", age)

# number of python topics studied so far
python_topics_done = 5        # integer value
print("python topics studied:", python_topics_done)


#----Float Examples----#

# Your average sleep hours
sleep_hours = 7.3    # float value  
print("Average slep hours:",sleep_hours)

# Your laptop screen size in inches
screen_size = 15.6      # float value
print("Laptop screen size:", screen_size)



# My goal:  daily coding time
daily_coding_goal = 6.3    # float value
print("Daily coding goal:", daily_coding_goal)




#----Complex Examples---#

# let's assume am simulating electric current in a basic circiut
current = 2+3j         # Real + imaginary part of a complex number 
print("simulated current in circuit:", current)      # Showing total simulated current in a circuit
print("Real part of a current:", current.real)       #Showing Real part 
print("Imaginary part of a current:", current.imag)   #Showing imaginary part




a3 = complex(3,6)   # a3 is a complex number with real part 3 and imaginary part 6
print(a3)           # prints the complex number
print(type(a3))     # prints the type of a3 (complex)
