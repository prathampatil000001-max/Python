# Problem 15: Username and Password Validation
# Ask the user for a username and password. Repeat the prompts until both fields meet all rules:

# Username must contain at least five characters after trimming outer spaces.
# Username must not contain internal spaces.
# Password must contain at least eight characters.
# Password must not be blank or consist only of spaces.
# Display a success message only when both fields are valid.
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    username = username.strip()

    if (len(username) >= 5 and " " not in username
            and len(password) >= 8 and password.strip() != ""):
        print("Username and password are valid!")
        break
    else:
        print("Invalid username or password. Please try again.")