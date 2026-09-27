# 14. Word Character Balance
# Take a sentence.

# For every word:

# Count vowels.
# Count consonants.
# If vowels > consonants → "Vowel Heavy"
# If consonants > vowels → "Consonant Heavy"
# Otherwise → "Balanced"
# Print the result for every word.

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    vowels = 0
    consonants = 0

    for ch in word.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    if vowels > consonants:
        result = "Vowel Heavy"
    elif consonants > vowels:
        result = "Consonant Heavy"
    else:
        result = "Balanced"

    print(word, "-> Vowels:", vowels,
          "Consonants:", consonants,
          "->", result)
