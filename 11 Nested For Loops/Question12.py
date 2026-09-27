# 12. Repeated Alphabet Pattern
# Write a Python program to print:

# A
# B B
# C C C
# D D D D
# E E E E E
# Hint
# Outer loop decides which alphabet to print.
# Inner loop repeats the same alphabet.
# Number of repetitions increases with each row.

for i in range(5):
    
    print((chr(65 + i) + " ") * (i + 1))
