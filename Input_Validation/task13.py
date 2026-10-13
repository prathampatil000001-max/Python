# Part B — Challenging Problems
# Problem 13: Integer Between 1 and 100
# Keep asking the user for an integer between 1 and 100, inclusive. Reject numbers outside the range and continue until a valid number is entered.
while True:
    num = int(input("Enter an integer between 1 and 100: "))

    if num >= 1 and num <= 100:
        print("Accepted number:", num)
        break
    else:
        print("Invalid number! Please enter a number between 1 and 100.")