# Python Input Validation — Practice Problems:-

# Intermediate and Challenging
# Topics covered

# Valid and invalid input
# Range validation
# Conditional validation
# Repeated input until valid
# while loops and break
# Combining conditions with and and or

# Part A — Intermediate Problems
# Problem 1: Valid Marks
# Ask the user to enter marks between 0 and 100, inclusive. If the marks are outside this range, keep asking until valid marks are entered. Finally, display the accepted marks.

while True:
    marks = int(input("Enter marks between 0 and 100: "))

    if 0 <= marks <= 100:
        print("Accepted marks:", marks)
        break
    else:
        print("Invalid marks! Please try again.")