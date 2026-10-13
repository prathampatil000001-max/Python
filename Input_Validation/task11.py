# Problem 11: Number Within a Range
# Keep asking for an integer between 10 and 50, inclusive. After accepting the value, print whether it is even or odd.
while True:
    num = int(input("Enter an integer between 10 and 50: "))

    if num >= 10 and num <= 50:
        print("Accepted number:", num)

        if num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

        break
    else:
        print("Invalid input! Please enter a number between 10 and 50.")