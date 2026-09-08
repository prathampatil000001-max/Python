#Question no.13


char = input("Enter one character: ")

if len(char) != 1 or not char.isalpha():
    print("Invalid input")
elif char.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
