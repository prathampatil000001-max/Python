# Q38. Smart Vehicle Dashboard
# Create a vehicle dashboard.

# Main options:

# 1 → Engine
# 2 → Lights
# 3 → Music
# 4 → Navigation
# For Engine:

# 1 → Start
# 2 → Stop
# For Lights:

# 1 → Headlights
# 2 → Indicators
# 3 → Hazard Lights
# For Music:

# 1 → Play
# 2 → Pause
# 3 → Next
# 4 → Previous
# For Navigation:

# 1 → Start Navigation
# 2 → Stop Navigation
# Use nested match-case.
choice = int(input("Enter your choice: "))

match choice:

    case 1:
        print("\n--- Engine ---")
        print("1. Start")
        print("2. Stop")

        engine_choice = int(input("Enter your choice: "))

        match engine_choice:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Engine Choice")

    case 2:
        print("\n--- Lights ---")
        print("1. Headlights")
        print("2. Indicators")
        print("3. Hazard Lights")

        light_choice = int(input("Enter your choice: "))

        match light_choice:
            case 1:
                print("Headlights ON")
            case 2:
                print("Indicators ON")
            case 3:
                print("Hazard Lights ON")
            case _:
                print("Invalid Lights Choice")

    case 3:
        print("\n--- Music ---")
        print("1. Play")
        print("2. Pause")
        print("3. Next")
        print("4. Previous")

        music_choice = int(input("Enter your choice: "))

        match music_choice:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Playing Next Song")
            case 4:
                print("Playing Previous Song")
            case _:
                print("Invalid Music Choice")

    case 4:
        print("\n--- Navigation ---")
        print("1. Start Navigation")
        print("2. Stop Navigation")

        navigation_choice = int(input("Enter your choice: "))

        match navigation_choice:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Navigation Choice")

    case _:
        print("Invalid Dashboard Choice")

