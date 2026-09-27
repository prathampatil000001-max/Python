# 9. Multiplication Grid
# Write a Python program to print:

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# Hint
# Outer loop represents numbers 1 to 3.
# Inner loop represents numbers 1 to 5.
# Multiply the two loop variables.

# Outer loop represents numbers 1 to 3
for i in range(1, 4):
    
    for j in range(1, 6):
        
        print(i * j, end=" ")
    
    print()
