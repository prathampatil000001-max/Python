# Problem 10: Limited PIN Attempts
# Set a secret PIN to 2468. Allow the user up to three attempts to enter the correct PIN. Stop immediately when the PIN is correct. If all attempts fail, display a message that access is denied.
secret_pin = "2468"
attempts = 0

while attempts < 3:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == secret_pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN! Try again.")

if attempts == 3 and pin != secret_pin:
    print("Access denied!")