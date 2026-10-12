# Challenge 1
# Write a program that keeps asking the user for numbers.

# Rules:

# Positive number → print it.
# Negative number → skip it using continue.
# 0 → stop using break.

numbers = [10, -2, 20, 0, 30]

for number in numbers:

    if number < 0:
        continue

    if number == 0:
        break

    print(number)