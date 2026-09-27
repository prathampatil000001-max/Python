# 14. Even Number Pattern
# Write a Python program to print:

# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
# Hint
# Outer loop controls rows.
# Inner loop generates even numbers.
# Think about the formula for the nth even number.

for i in range(1, 6):
    
    for j in range(2, (2 * i) + 1, 2):
        print(j, end=" ")
    print()
