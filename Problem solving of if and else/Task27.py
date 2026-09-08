day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12 or day < 1:
    print("Invalid date")

elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if day <= 29:
            print("Valid date")
        else:
            print("Invalid date")
    else:
        if day <= 28:
            print("Valid date")
        else:
            print("Invalid date")

elif month == 4 or month == 6 or month == 9 or month == 11:
    if day <= 30:
        print("Valid date")
    else:
        print("Invalid date")

else:
    if day <= 31:
        print("Valid date")
    else:
        print("Invalid date")


    