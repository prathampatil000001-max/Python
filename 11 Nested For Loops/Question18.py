# 18. Print 1 to 20 in 4 Rows
# Write a Python program to print numbers from 1 to 20 in 4 rows, with 5 numbers in each row.

# Expected output:

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# Hint
# Outer loop should create 4 rows.
# Inner loop should print 5 numbers per row.
# Keep one number variable that continues increasing.
# Create a tracking counter variable before starting the loops
counter = 1

for i in range(4):
    
    for j in range(5):
        
        print(counter, end=" ")
        counter += 1
    print()  
    
   
