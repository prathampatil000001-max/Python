# 17. Row-wise Numbers
# Write a Python program to print:

# 1 2 3
# 4 5 6
# 7 8 9
# Hint
# Create a number variable before the loops.
# Print the number inside the inner loop.
# Increase the number after every print.
# Create a tracking counter variable before starting the loops
counter = 1

for i in range(3):
    
    for j in range(3):
        
        print(counter, end=" ")
        
        counter += 1
    
    print()
