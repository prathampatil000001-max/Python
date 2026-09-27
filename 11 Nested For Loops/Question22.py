# 22. Repeated Number Pattern
# Write a Python program to print:

# 1
# 22
# 333
# 4444
# 55555
# Hint
# Outer loop decides the number.
# Inner loop decides how many times the number is printed.
# Number of repetitions is equal to the current row.


for i in range(1, 6):
    
    print(str(i) * i)
