# Topic 10 — Challenge Problems
# Q35. Restaurant Ordering System
# Create a restaurant ordering system.

# First select a category:

# 1 → Starters
# 2 → Main Course
# 3 → Desserts
# 4 → Drinks
# Then show different items for each category.

# Example:

# Starters:

# 1 → Soup
# 2 → Spring Roll
# 3 → Garlic Bread
# Main Course:

# 1 → Pizza
# 2 → Pasta
# 3 → Biryani
# Desserts:

# 1 → Ice Cream
# 2 → Cake
# 3 → Gulab Jamun
# Drinks:

# 1 → Coffee
# 2 → Tea
# 3 → Juice
# Use nested match-case.

category = int(input("Select category: "))

match category:

    case 1:
        print("1. Soup")
        print("2. Spring Roll")
        print("3. Garlic Bread")

        item = int(input("Select item: "))

        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Item")

    case 2:
        print("1. Pizza")
        print("2. Pasta")
        print("3. Biryani")

        item = int(input("Select item: "))

        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Item")

    case 3:
        print("1. Ice Cream")
        print("2. Cake")
        print("3. Gulab Jamun")

        item = int(input("Select item: "))

        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Item")

    case 4:
        print("1. Coffee")
        print("2. Tea")
        print("3. Juice")

        item = int(input("Select item: "))

        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Item")

    case _:
        print("Invalid Category")