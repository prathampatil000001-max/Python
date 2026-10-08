# Q29. Library Management System
# Create a library menu:

# 1 → Search Book
# 2 → Issue Book
# 3 → Return Book
# 4 → View Issued Books
# 5 → Exit
# Use match-case to process the user's choice.
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Search Book selected.")
    case 2:
        print("Issue Book selected.")
    case 3:
        print("Return Book selected.")
    case 4:
        print("View Issued Books selected.")
    case 5:
        print("Exiting Library Management System...")
    case _:
        print("Invalid choice.")

