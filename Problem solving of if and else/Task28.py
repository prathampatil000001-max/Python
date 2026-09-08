hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if (0 <= hours <= 23 and
    0 <= minutes <= 59 and
    0 <= seconds <= 59):
    print("Valid time")
else:
    print("Invalid time")
