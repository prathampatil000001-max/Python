# Problem 9: Divisible Number
# Keep asking the user for a positive integer that is divisible by both 3 and 5. Reject all other values. Display the accepted number.
while True:
    num = int(input("Enter a positive integer divisible by both 3 and 5: "))

    if num > 0 and num % 3 == 0 and num % 5 == 0:
        print("Accepted number:", num)
        break
    else:
        print("Invalid input! Please try again.")