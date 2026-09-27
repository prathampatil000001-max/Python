# 6. Increasing Number Pattern
# Write a Python program to print:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Hint
# Outer loop represents the row.
# Inner loop starts from 1 and ends at the current row number.

# Outer loop controls the total number of rows (1 to 5)
for i in range(1, 6):
   
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  
