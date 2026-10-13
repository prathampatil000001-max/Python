# Problem 2: Positive Integer
# Keep asking the user to enter an integer until they enter a number greater than 0. Display the accepted number.
while True:
    num = int(input("Enter a positive integer: "))

    if num > 0:
        print("Accepted number:", num)
        break
    else:
        print("Invalid input! Please enter a number greater than 0.")