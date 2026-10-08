# Q6. Online Shopping Menu
# Create an online shopping menu:

# 1 → Electronics
# 2 → Clothing
# 3 → Books
# 4 → Grocery
# 5 → Exit

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")
