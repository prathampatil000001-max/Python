# 8. Multiplication Tables from 1 to 5
# Write a Python program to print multiplication tables from 1 to 5.

# Each table should contain multiplication from 1 to 10.

# Hint
# Outer loop selects the table number.
# Inner loop runs from 1 to 10.
# Multiply the outer-loop number by the inner-loop number.

# Outer loop selects the table number (1 to 5)
for i in range(1, 6):
    print(f"--- Multiplication Table of {i} ---")
    
    
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}")
        
    print()  
