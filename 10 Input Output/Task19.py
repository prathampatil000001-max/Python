
#Question no.19

number = float(input("Enter a number: "))

if number < 0:
    print("Negative")
elif number <= 10:
    print("0–10")
elif number <= 50:
    print("11–50")
elif number <= 100:
    print("51–100")
else:
    print("Above 100")
