# Problem 14: Marks and Result
# Keep asking the user for marks between 0 and 100, inclusive. After accepting valid marks, display:

# Distinction for marks of 75 or more.
# First Class for marks of 60 to less than 75.
# Pass for marks of 35 to less than 60.
# Fail for marks below 35.
# Do not calculate the result until the marks are valid.
while True:
    marks = int(input("Enter marks between 0 and 100: "))

    if marks >= 0 and marks <= 100:
        break
    else:
        print("Invalid marks! Please try again.")

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")