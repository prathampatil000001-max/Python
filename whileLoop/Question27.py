# Use nested loops to print:

# *****
# *****
# *****
# *****
row = 1

while row <= 4:
    column = 1

    while column <= 5:
        print("*", end="")
        column = column + 1

    print()
    row = row + 1