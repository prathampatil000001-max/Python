# 8. Shopping Cart Analyzer
# Take prices of 8 products.

# For every price:

# Below 500 → "Budget"
# 500–1999 → "Regular"
# 2000–4999 → "Premium"
# 5000 or more → "Luxury"
# Calculate:

# Total amount.
# Number of products in each category.
# Average product price.


total = 0

budget = 0
regular = 0
premium = 0
luxury = 0

for i in range(8):
    price = float(input(f"Enter price of product {i + 1}: "))

    total += price

    if price < 500:
        budget += 1
        category = "Budget"
    elif price < 2000:
        regular += 1
        category = "Regular"
    elif price < 5000:
        premium += 1
        category = "Premium"
    else:
        luxury += 1
        category = "Luxury"

    print("Category:", category)
                                
average = total / 8

print("\nTotal amount:", total)
print("Budget products:", budget)
print("Regular products:", regular)
print("Premium products:", premium)
print("Luxury products:", luxury)
print("Average product price:", average)
