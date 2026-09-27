# 5. Decreasing Star Pattern
# Write a Python program to print:

# * * * * *
# * * * *
# * * *
# * *
# *
# Hint
# Start with 5 stars.
# Reduce the number of stars by 1 after every row.


for i in range(5, 0, -1):
   
    for j in range(i):
        print("*", end=" ")
    print()  

