# Q36. Digital Payment Application
# Create a digital payment application.

# Payment type:

# 1 → UPI
# 2 → Card
# 3 → Wallet
# If UPI is selected:

# 1 → Scan QR
# 2 → Enter UPI ID
# If Card is selected:

# 1 → Credit Card
# 2 → Debit Card
# If Wallet is selected:

# 1 → Add Money
# 2 → Pay Using Wallet
# Use nested match-case.
payment_type = int(input("Select payment type: "))

match payment_type:

    case 1:
        print("1. Scan QR")
        print("2. Enter UPI ID")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1. Credit Card")
        print("2. Debit Card")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1. Add Money")
        print("2. Pay Using Wallet")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Payment Type")