# 6. Number-String Conversion Challenge
# Take 5 numbers from the user.

# For each number:

# Convert it to a string.
# Examine every digit using a loop.
# Count even and odd digits.
# Print which type occurs more.
# If equal, print "Equal"


for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))


    num_str = str(number)

    even_count = 0
    odd_count = 0

    
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even digits:", even_count)
    print("Odd digits:", odd_count)

    if even_count > odd_count:
        print("Even occurs more")
    elif odd_count > even_count:
        print("Odd occurs more")
    else:
        print("Equal")
