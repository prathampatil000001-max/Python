# 28.
# Print the following pattern:

# *
# **
# ***
# ****
# *****
row = 1

while row <= 5:
    column = 1

    while column <= row:
        print("*", end="")
        column = column + 1

    print()
    row = row + 1