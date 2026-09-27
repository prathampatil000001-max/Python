# 29.
# Print the following pattern:

# 1
# 12
# 123
# 1234
# 12345
row = 1

while row <= 5:
    column = 1

    while column <= row:
        print(column, end="")
        column = column + 1

    print()
    row = row + 1