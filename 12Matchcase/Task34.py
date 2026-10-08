# Q34. Gaming Console Menu
# Create a gaming console menu:

# 1 → Start Game
# 2 → Load Game
# 3 → Settings
# 4 → Exit
# If Settings is selected, show:

# 1 → Sound
# 2 → Graphics
# 3 → Controls
# Use nested match-case for the Settings menu.
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Start Game Selected")

    case 2:
        print("Load Game Selected")

    case 3:
        print("1. Sound")
        print("2. Graphics")
        print("3. Controls")

        setting = int(input("Enter setting option: "))

        match setting:
            case 1:
                print("Sound Selected")
            case 2:
                print("Graphics Selected")
            case 3:
                print("Controls Selected")
            case _:
                print("Invalid Settings Option")
        
    case 4:
        print("Exit Selected")

    case _:
        print("Invalid Choice")

