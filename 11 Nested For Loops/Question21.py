# 21. 10×10 Multiplication Grid
# Write a Python program to print a multiplication grid from 1 to 10.

# Hint
# Both loops should run from 1 to 10.
# Multiply the outer-loop value by the inner-loop value.
# Use spacing or tabs to make the output readable.

# Outer loop represents rows (1 to 10)
for i in range(1, 11):
    
    for j in range(1, 11):
        
        product = i * j
        
        print(f"{product:4}", end="")
    
    print()
