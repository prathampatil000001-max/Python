# Topic 9 — More Challenging Problems
# Q31. Banking Application with Nested Menu
# Create a banking application.

# Main menu:

# 1 → Personal Banking
# 2 → Business Banking
# Personal Banking:

# 1 → Balance
# 2 → Transfer
# 3 → Loan
# Business Banking:

# 1 → Balance
# 2 → Payroll
# 3 → Business Loan
# Use nested match-case.

# Sample Input
# Enter banking type: 2
# Enter option: 3
# Sample Output
# Business Loan Selected

banking_type = int(input("Enter banking type: "))

match banking_type:
    case 1:
        print("1. Balance")
        print("2. Transfer")
        print("3. Loan")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Transfer Selected")
            case 3:
                print("Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1. Balance")
        print("2. Payroll")
        print("3. Business Loan")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")

