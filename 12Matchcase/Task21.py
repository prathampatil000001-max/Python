# Q21. Temperature Converter
# Create a converter:

# 1 → Celsius to Fahrenheit
# 2 → Fahrenheit to Celsius
# Take the temperature and perform the selected conversion.

# Sample Input
# Enter choice: 1
# Enter temperature: 25
# Sample Output
# Temperature = 77.0 F
choice = int(input("Enter choice: "))
temperature = float(input("Enter temperature: "))

match choice:
    case 1:
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature =", fahrenheit, "F")

    case 2:
        celsius = (temperature - 32) * 5 / 9
        print("Temperature =", celsius, "C")

    case _:
        print("Invalid choice")
                              
