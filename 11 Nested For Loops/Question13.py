# 13. Odd Number Pattern
# Write a Python program to print:

# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
# Hint
# Outer loop controls the number of values in each row.
# Inner loop generates odd numbers.
# Think about the formula for the nth odd number.


for i in range(1, 6):
    
    for j in range(1, 2 * i, 2):
        print(j, end=" ")
    print()