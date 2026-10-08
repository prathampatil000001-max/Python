# Q27. Hospital Department Selection
# Create a hospital department menu:

# 1 → General Medicine
# 2 → Cardiology
# 3 → Orthopedics
# 4 → Pediatrics
# 5 → Emergency
# Display the selected department.

# For invalid input, display:

# Invalid Department
department = int(input("Enter department: "))

match department:
    case 1:
        print("General Medicine")

    case 2:
        print("Cardiology")

    case 3:
        print("Orthopedics")

    case 4:
        print("Pediatrics")

    case 5:
        print("Emergency")

    case _:
        print("Invalid Department")
