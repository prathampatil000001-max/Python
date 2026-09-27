# 20. Print All Number Combinations
# For numbers from 1 to 3, print every possible pair:

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# Hint
# Both loops should run from 1 to 3.
# The inner loop must complete all values before the outer loop moves to the next value.

# Outer loop runs from 1 to 3
for i in range(1, 4):
    
    for j in range(1, 4):
       
        print(i, j)
