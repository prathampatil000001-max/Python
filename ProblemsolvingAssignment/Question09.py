# 9. Character Position Challenge
# Take a string.

# For every character, print:

# Character
# Position
# Whether position is even or odd
# Whether character is vowel, consonant, digit, or special character
# At the end, count how many characters fall into each category.




text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for position in range(len(text)):
    ch = text[position]

    
    if (position + 1) % 2 == 0:
        position_type = "Even"
    else:
        position_type = "Odd"

    
    if ch.isalpha():
        if ch.lower() in "aeiou":
            char_type = "Vowel"
            vowels += 1
        else:
            char_type = "Consonant"
            consonants += 1

    elif ch.isdigit():
        char_type = "Digit"
        digits += 1

    else:
        char_type = "Special character"
        special += 1
                                         
    print("Character:", ch)
    print("Position:", position)
    print("Position type:", position_type)
    print("Character type:", char_type)
    print()

print("----- Total Count -----")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)
