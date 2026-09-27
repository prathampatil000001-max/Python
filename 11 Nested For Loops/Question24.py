# 24. Reverse Number Pattern
# Write a Python program to print:

# 54321
# 5432
# 543
# 54
# 5
# Hint
# Outer loop controls how many numbers are printed.
# Inner loop should print numbers in decreasing order.

base_string = "54321"

for i in range(5, 0, -1):
    print(base_string[:i])
