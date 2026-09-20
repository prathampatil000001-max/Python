#Quetion no. 12

char = input("Enter one character: ")

if char.isupper() and char.isalpha():
    print("Uppercase alphabet")
elif char.islower() and char.isalpha():
    print("Lowercase alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")
