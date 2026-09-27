# 7. Repeated Number Pattern
# Write a Python program to print:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# Hint
# The outer loop gives the number to print.
# The inner loop repeats that number according to the row number.

# Outer loop controls the row number and the value to print (1 to 5)
for i in range(1, 6):
    
    for j in range(i):
        print(i, end=" ")
    print() 