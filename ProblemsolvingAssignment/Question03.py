#  3. Word Score Calculator
# # Take a sentence.

# For every word:

# Vowel = 2 points.
# Consonant = 1 point.
# Digit = 3 points.
# Special character = 4 points.
# Calculate the score of every word and print the word with the highest score.
# Do not use max().



sentence = input("Enter a sentence: ")

words = sentence.split()

highest_word = ""
highest_score = 0

for word in words:
    score = 0

    for ch in word:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                score += 2
            else:
                score += 1
        elif ch.isdigit():
            score += 3
        else:
            score += 4

    if score > highest_score:
        highest_score = score
        highest_word = word

print("Word with highest score:", highest_word)
print("Score:", highest_score)
