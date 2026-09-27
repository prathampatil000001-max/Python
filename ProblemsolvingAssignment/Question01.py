# 1. Digit and Character Analyzer
# Take a string containing letters, digits, spaces, and special characters.

# Using a for loop:

# Count uppercase letters.
# Count lowercase letters.
# Count digits.
# Count spaces.
# Count special characters.
# Print which category has the highest count.
# If two or more categories have the same highest count, print "Tie".

s = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        special += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

counts = {
    "Uppercase letters": uppercase,
    "Lowercase letters": lowercase,
    "Digits": digits,
    "Spaces": spaces,
    "Special characters": special
}

highest = max(counts.values())
categories = [category for category, count in counts.items() if count == highest]

if len(categories) > 1:
    print("Tie")
else:
    print("Highest count:", categories[0])
