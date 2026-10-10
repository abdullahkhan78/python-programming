# Binary data types in Python
# Includes: bytes, bytearray, memoryview

# =========== bytes example ==================

# Example_1

byte1 = "gargi"         # byte1 is just a regular string, not actual binary data
print(byte1)            # prints the string
print(type(byte1))      # prints the type (str)


# Example_2
# Convert from string to bytes
text = "Hello"
bytes_data = text.encode()    # Convert string to bytes
print(bytes_data)                # b'Hello'
print(type(bytes_data))  # <class 'bytes'>



#============ bytearray example ==============

data = bytearray([65, 66, 67])  # Creates a bytearray with ASCII values (A=65, B=66, C=67)
print(data)                     # Output: bytearray(b'ABC')
print(type(data))               # Output: <class 'bytearray'>



# Example_2
# Create a bytearray from bytes
byte_arr = bytearray(b"Hello")
print(byte_arr)               # bytearray(b'Hello')
print(type(byte_arr))         # <class 'bytearray'>

# Change the first character
byte_arr[0] = 74               # ASCII 74 = 'J'
print(byte_arr)               # bytearray(b'Jello')



# ============= memoryview example ==============
view = memoryview(data)         # Creates a memoryview of the bytearray
print(view[0])                  # Output: 65 (the first byte)
print(view[1])                  # Output: 66
print(type(view))               # Output: <class 'memoryview'>
