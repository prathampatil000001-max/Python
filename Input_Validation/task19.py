# Problem 19: Product Quantity and Price
# Ask the user for a product quantity and unit price.


quantity = int(input("Enter product quantity: "))
price = float(input("Enter unit price: ₹"))

if quantity > 0 and price > 0:
    total = quantity * price
    print("Total cost: ₹", total)
else:
    print("Invalid input. Quantity and price must be greater than zero.")