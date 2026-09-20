age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

eligible = True

if age < 18 or age > 25:
    print("Failed: Age must be between 18 and 25.")
    eligible = False

if marks < 85:
    print("Failed: Marks must be above 85.")
    eligible = False

if attendance < 75:
    print("Failed: Attendance must be  above 75.")
    eligible = False

if income > 300000:
    print("Failed: Family income must be  below 300000.")
    eligible = False

if eligible:
    print("Scholarship approved.")
else:
    print("Scholarship not approved.")
