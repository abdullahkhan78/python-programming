import random
import string

password_length = 15

characters = string.digits + string.punctuation + string.ascii_letters

password = "".join(random.choice(characters) for i in range(password_length))

print("Your random password is:",password)