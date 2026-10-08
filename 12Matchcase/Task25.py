# Q25. Movie Ticket System
# Create a movie ticket menu:

# 1 → Regular
# 2 → Premium
# 3 → VIP
# Ask for the customer's age after selecting the ticket type.

# If age is below 5, display:

# Free Entry
# Otherwise display the selected ticket type.

# Use match-case for ticket selection and if for the age condition
ticket_type = int(input("Enter ticket type: "))

match ticket_type:
    case 1:
        ticket = "Regular"
        age = int(input("Enter age: "))

        if age < 5:
            print("Free Entry")
        else:
            print("Regular Ticket")

    case 2:
        ticket = "Premium"
        age = int(input("Enter age: "))

        if age < 5:
            print("Free Entry")
        else:
            print("Premium Ticket")

    case 3:
        ticket = "VIP"
        age = int(input("Enter age: "))

        if age < 5:
            print("Free Entry")
        else:
            print("VIP Ticket")

    case _:
        print("Invalid ticket type")
