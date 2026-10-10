# First nested loop: Increasing star pattern
rows = 8  # Total number of rows

# Outer loop → controls the number of rows
for i in range(1, rows - 1):
    # Inner loop → prints stars according to the row number

    for j in range(i):
        print("*", end="")  # Print stars in the same line
    print()  # Move to the next line after inner loop finishes





# Second nested loop: Decreasing star pattern
# Outer loop → starts from 'rows' and decreases to 1
for i in range(rows, 0, -1):

    # Inner loop → prints stars according to the row number

    for j in range(i):
        print("*", end="")  # Print stars in the same line
    print()  # Move to the next line after inner loop finishes
