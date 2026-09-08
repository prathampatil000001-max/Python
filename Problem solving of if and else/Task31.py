age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

eligible = True

if age < 18 or age > 25:
    print("Failed: Age must be between 18 and 25.")
    eligible = False

if marks < 85:
    print("Failed: Marks must be 85 or above.")
    eligible = False

if attendance < 75:
    print("Failed: Attendance must be 75% or above.")
    eligible = False

if income > 300000:
    print("Failed: Family income must be ₹300000 or below.")
    eligible = False

if eligible:
    print("Scholarship approved.")
else:
    print("Scholarship not approved.")
