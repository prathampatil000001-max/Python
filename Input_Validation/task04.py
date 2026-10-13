# Problem 4: Menu Choice
# Display this menu repeatedly until the user enters a valid choice:

# 1. View profile
# 2. Edit profile
# 3. Settings
# 4. Exit
# Accept only the integers 1, 2, 3, and 4. Display the selected option after valid input.
while True:
    print("\nMenu")
    print("1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice >= 1 and choice <= 4:
        print("Selected option:", choice)
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")