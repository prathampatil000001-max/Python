marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

# Check whether marks are valid
if (marks1 < 0 or marks1 > 100 or
    marks2 < 0 or marks2 > 100 or
    marks3 < 0 or marks3 > 100):
    print("Invalid marks")

# Check whether the student has failed
elif marks1 < 35 or marks2 < 35 or marks3 < 35:
    print("Fail")

else:
    average = (marks1 + marks2 + marks3) / 3

    print("Average =", average)

    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass")
