# Problem 5: Password Length
# Keep asking the user for a password until it contains at least eight characters. Leading and trailing spaces should not count toward the password length. Display a success message after valid input.

while True:
    password = input("Enter your password: ").strip()

    if len(password) >= 8:
        print("Password accepted successfully!")
        break
    else:
        print("Invalid password! It must contain at least 8 characters.")