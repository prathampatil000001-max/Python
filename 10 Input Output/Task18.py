#Question no .18

temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing")
elif temperature <= 15:
    print("Very Cold")
elif temperature <= 25:
    print("Cold")
elif temperature <= 35:
    print("Normal")
else:
    print("Hot")
