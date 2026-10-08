# Q33. Travel Booking System
# Create a travel booking system.

# Select transport:

# 1 → Flight
# 2 → Train
# 3 → Bus
# Then show options:

# Flight:

# 1 → Economy
# 2 → Business
# Train:

# 1 → Sleeper
# 2 → AC
# Bus:

# 1 → Ordinary
# 2 → Volvo
# Use nested match-case.

transport = int(input("Select transport: "))

match transport:

    case 1:
        print("1. Economy")
        print("2. Business")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Economy Selected")
            case 2:
                print("Business Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1. Sleeper")
        print("2. AC")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Sleeper Selected")
            case 2:
                print("AC Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1. Ordinary")
        print("2. Volvo")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Ordinary Selected")
            case 2:
                print("Volvo Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Transport")
        

