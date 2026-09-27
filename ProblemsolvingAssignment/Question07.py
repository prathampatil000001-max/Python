# 7. Repeated Character Report
# Take a string.

# For every character, determine how many times it appears in the string without using count().

# Print only characters that appear more than once.

# Also classify them:

# 2 occurrences → "Duplicate"
# 3–4 occurrences → "Repeated"
# More than 4 → "Highly Repeated"


text = input("Enter a string: ")

checked = ""

for ch in text:
    if ch not in checked:
        frequency = 0

        
        for x in text:
            if x == ch:
                frequency += 1

        
        if frequency > 1:
            if frequency == 2:
                category = "Duplicate"
            elif frequency <= 4:
                category = "Repeated"
            else:
                category = "Highly Repeated"

            print(ch, "->", frequency, "occurrences ->", category)

        checked += ch
