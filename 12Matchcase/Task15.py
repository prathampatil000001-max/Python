# Q15. Store Discount Category
# A store uses membership levels:

# 1 → Bronze
# 2 → Silver
# 3 → Gold
# 4 → Platinum
# Group the levels:

# 1, 2 → Basic Membership
# 3, 4 → Premium Membership
# Display the appropriate category.
level = int(input("Enter membership level (1-4): "))

if level == 1 or level == 2:
    print("Basic Membership")
elif level == 3 or level == 4:
    print("Premium Membership")
else:
    print("Invalid membership level")
