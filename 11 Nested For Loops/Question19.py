# 19. Print Coordinate Pairs
# Write a Python program to print:

# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)
# Hint
# Outer loop represents the first coordinate.
# Inner loop represents the second coordinate.
# Print both loop variables together.

for i in range(1, 4):
    
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
            
    print()
        
        