# Problem 6: Temperature Range
# Ask the user to enter a temperature between -20 and 45, inclusive. Reject values outside the range and repeat the prompt until the input is valid.
while True:
    temperature = float(input("Enter temperature between -20 and 45: "))

    if temperature >= -20 and temperature <= 45:
        print("Accepted temperature:", temperature)
        break
    else:
        print("Invalid temperature! Please try again.")