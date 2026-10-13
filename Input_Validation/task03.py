# Problem 3: Age Validation
# Ask the user to enter their age. Accept ages from 0 through 120. If the age is outside this range, display an error message and ask again.
while True:
    age = int(input("Enter your age: "))

    if age >= 0 and age <= 120:
        print("Accepted age:", age)
        break
    else:
        print("Invalid age! Please enter an age between 0 and 120.")