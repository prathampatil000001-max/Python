# Challenge 2
# Given:

# numbers = [12, 5, -4, 18, 0, 25, 30]
# Process the list using these rules:

# Negative number → skip.
# 0 → stop.
# Positive number → print.

number=[12,5,-4,18,0,25,30]

for number in number:

    if number < 0:
        continue

    if number == 0:
        break

    print(number)