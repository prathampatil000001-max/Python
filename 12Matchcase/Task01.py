# Q1. Food Ordering System
# A restaurant has the following menu:

# 1 → Pizza
# 2 → Burger
# 3 → Pasta
# 4 → Sandwich
# Write a program that takes the customer's choice and displays the selected food.

# If the customer enters any other number, display:

# Invalid Menu Choice

choice = 2

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case _:
        print("Sandwich")
