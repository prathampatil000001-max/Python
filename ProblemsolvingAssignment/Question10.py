# 10. Number Pattern With Conditions
# Take n.

# Print a pattern where each row contains numbers from 1 to the row number.

# Replace:

# Multiples of 3 with X
# Multiples of 5 with Y
# Multiples of both 3 and 5 with Z

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 15 == 0:
            print("Z", end=" ")
        elif j % 3 == 0:
            print("X", end=" ")
        elif j % 5 == 0:
            print("Y", end=" ")
        else:
            print(j, end=" ")
    print()
