# Problem 8: Username Validation
# Keep asking for a username until it:

# Contains at least five characters after removing leading and trailing spaces.
# Is not empty.
# Does not contain a space inside the username.
# Display the accepted username.
while True:
    username = input("Enter your username: ").strip()

    if len(username) >= 5 and username != "" and " " not in username:
        print("Accepted username:", username)
        break
    else:
        print("Invalid username!")
        print("Username must have at least 5 characters and no spaces inside.")