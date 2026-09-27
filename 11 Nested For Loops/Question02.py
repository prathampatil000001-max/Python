# 2. Print Numbers in Rows
# Write a Python program to print:

# 1 2 3
# 1 2 3
# 1 2 3
# Hint
# Outer loop controls the 3 rows.
# Inner loop should print numbers from 1 to 3.

# Loop for 3 rows
for i in range(3):
    
    for j in range(1, 4):
        print(j, end=" ")
    print()  
