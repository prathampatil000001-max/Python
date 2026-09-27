# 3. Print Row Numbers
# Write a Python program to print:

# 1 1 1
# 2 2 2
# 3 3 3
# Hint
# Outer loop should represent the row number.
# Inner loop should repeat the current row number 3 times.


for i in range(1, 4):
    
    for j in range(3):
        print(i, end=" ")
    print() 
 
    