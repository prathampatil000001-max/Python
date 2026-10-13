# Problem 18: Validate Month and Day
# Ask the user to enter a month number from 1 to 12 and a day number from 1 to 31. Keep asking until both values are within their individual ranges.
while True:
    month = int(input("Enter month number (1-12): "))

    if 1 <= month <= 12:
        break
    print("Invalid month. Please enter a number from 1 to 12.")

while True:
    day = int(input("Enter day number (1-31): "))

    if 1 <= day <= 31:
        break
    print("Invalid day. Please enter a number from 1 to 31.")

print("Valid month and day entered!")
print("Month:", month)
print("Day:", day)