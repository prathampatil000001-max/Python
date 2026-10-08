# Topic 11 — Mixed Logic Challenge
# Q39. Employee Portal
# Create an employee portal.

# Main menu:

# 1 → Employee
# 2 → Manager
# Employee options:

# 1 → View Profile
# 2 → Apply Leave
# 3 → View Salary
# Manager options:

# 1 → View Team
# 2 → Approve Leave
# 3 → View Reports
# Use nested match-case.

# For the Apply Leave option, ask for the number of leave days.

# Use if to check:

# If leave days are greater than 0, display Leave Request Submitted.
# Otherwise display Invalid Leave Days.
# This problem should use both match-case and if.


main_choice = int(input("Enter your choice: "))

match main_choice:

    case 1:
        print("\n--- Employee Menu ---")
        print("1. View Profile")
        print("2. Apply Leave")
        print("3. View Salary")

        employee_choice = int(input("Enter your choice: "))

        match employee_choice:
            case 1:
                print("Employee Profile")

            case 2:
                leave_days = int(input("Enter number of leave days: "))

                if leave_days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")

            case 3:
                print("Employee Salary")

            case _:
                print("Invalid Employee Choice")

    case 2:
        print("\n--- Manager Menu ---")
        print("1. View Team")
        print("2. Approve Leave")
        print("3. View Reports")

        manager_choice = int(input("Enter your choice: "))

        match manager_choice:
            case 1:
                print("Team Details")

            case 2:
                print("Leave Approved")

            case 3:
                print("Manager Reports")

            case _:
                print("Invalid Manager Choice")

    case _:
        print("Invalid Main Menu Choice")