# Challenge 3
# Write a program that searches for a number in a list.

# If found:

# Number found
# If the loop finishes without finding it:

# Number not found

number=[12,5,-4,18,0,25,30]

for number in number:

    if number < 0:
        continue

    if number == 0:
        break

    print("number not found")