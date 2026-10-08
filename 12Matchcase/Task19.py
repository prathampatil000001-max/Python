# Q19. Food Delivery Application
# First ask:

# 1 → Vegetarian
# 2 → Non-Vegetarian
# If Vegetarian:

# 1 → Paneer
# 2 → Dal
# 3 → Veg Biryani
# If Non-Vegetarian:

# 1 → Chicken Biryani
# 2 → Chicken Curry
# 3 → Fish Fry
# Use nested match-case.

# Sample Input
# Enter category: 2
# Enter food: 1
# Sample Output
# Chicken Biryani Selected

category = int(input("Enter category: "))

match category:
    case 1:
        print("Vegetarian")
        food = int(input("Enter food: "))

        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid food choice")

    case 2:
        print("Non-Vegetarian")
        food = int(input("Enter food: "))

        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid food choice")

    case _:
        print("Invalid category")
