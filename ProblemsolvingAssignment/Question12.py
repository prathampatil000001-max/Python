# 12. Vowel-Consonant Battle
# Take a sentence.

# Count vowels and consonants.

# Then:

# Print "Vowels Win" if vowels are greater.
# Print "Consonants Win" if consonants are greater.
# Print "Draw" if equal.
# Also print the frequency of each vowel.

sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for ch in sentence.lower():

    if ch in "aeiou":
        vowels += 1

        if ch == "a":
            a_count += 1
        elif ch == "e":
            e_count += 1
        elif ch == "i":
            i_count += 1
        elif ch == "o":
            o_count += 1
        elif ch == "u":
            u_count += 1

    elif ch.isalpha():
        consonants += 1

print("\nVowels:", vowels)
print("Consonants:", consonants)

print("\nVowel Frequency:")
print("a:", a_count)
print("e:", e_count)
print("i:", i_count)
print("o:", o_count)
print("u:", u_count)

if vowels > consonants:
    print("\nVowels Win")
elif consonants > vowels:
    print("\nConsonants Win")
else:
    print("\nDraw")
