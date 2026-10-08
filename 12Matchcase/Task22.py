# Q22. Unit Converter
# Create a unit conversion menu:

# 1 → Kilometers to Meters
# 2 → Meters to Kilometers
# 3 → Kilograms to Grams
# 4 → Grams to Kilograms
# Take the required value and perform the selected conversion.

# Sample Input
# Enter choice: 1
# Enter value: 5
# Sample Output
# 5000 meters
choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

match choice:
    case 1:
        meters = value * 1000
        print(meters, "meters")

    case 2:
        kilometers = value / 1000
        print(kilometers, "kilometers")

    case 3:
        grams = value * 1000
        print(grams, "grams")

    case 4:
        kilograms = value / 1000
        print(kilograms, "kilograms")

    case _:
        print("Invalid choice")
