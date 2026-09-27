# 23. Decreasing Number Pattern
# Write a Python program to print:

# 12345
# 1234
# 123
# 12
# 1
# Hint
# Outer loop should decrease from 5 to 1.
# Inner loop should print numbers starting from 1.
# The number of values printed decreases every row.
base_string = "12345"

for i in range(5, 0, -1):
    print(base_string[:i])
