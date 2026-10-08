# Q37. Online Learning Platform
# Create an online learning platform.

# First select:

# 1 → Programming
# 2 → Mathematics
# 3 → Communication
# Programming:

# 1 → Python
# 2 → Java
# 3 → C++
# Mathematics:

# 1 → Algebra
# 2 → Calculus
# 3 → Statistics
# Communication:

# 1 → English
# 2 → Presentation
# 3 → Interview Skills
# Use nested match-case.

category = int(input("Select category: "))

match category:

    case 1:
        print("1. Python")
        print("2. Java")
        print("3. C++")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1. Algebra")
        print("2. Calculus")
        print("3. Statistics")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1. English")
        print("2. Presentation")
        print("3. Interview Skills")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Category")