# 11. Alphabet Pattern
# Write a Python program to print:

# A
# A B
# A B C
# A B C D
# A B C D E
# Hint
# Outer loop controls the number of characters in each row.
# Inner loop starts from A and prints up to the required character.

alphabet = "A B C D E"

for i in range(1, 6):
    
    print(alphabet[:i * 2].strip())
