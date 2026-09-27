# 13. Electricity Bill Calculator
# Take electricity usage for 6 customers.

# Calculate the bill using:

# First 100 units → ₹5/unit
# Next 100 units → ₹7/unit
# Next 200 units → ₹10/unit
# Above 400 units → ₹15/unit
# Also classify:

# Below ₹1000 → "Low"
# ₹1000–₹3000 → "Medium"
# Above ₹3000 → "High"
# Print total revenue.


total_revenue = 0

for i in range(6):
    units = int(input(f"Enter electricity units for customer {i + 1}: "))


    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    elif units <= 400:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    else:
        bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 15)

    
    if bill < 1000:
        category = "Low"
    elif bill <= 3000:
        category = "Medium"
    else:
        category = "High"

    total_revenue += bill

    print("Bill:", bill)
    print("Category:", category)
    print()

print("Total Revenue: ₹", total_revenue)
