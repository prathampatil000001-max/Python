# Q18. E-Commerce Application
# First ask for a category:

# 1 → Electronics
# 2 → Clothing
# For Electronics:

# 1 → Mobile
# 2 → Laptop
# 3 → Headphones
# For Clothing:

# 1 → Shirt
# 2 → Jeans
# 3 → Shoes
# Use nested match-case.

# Sample Input
# Enter category: 1
# Enter product: 2
# Sample Output
# Laptop Selected

category = int(input("Enter category: "))

match category:
    case 1:
        product = int(input("Enter product: "))

        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid product")

    case 2:
        product = int(input("Enter product: "))

        match product:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid product")

    case _:
        print("Invalid category")

