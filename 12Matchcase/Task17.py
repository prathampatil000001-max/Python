# Q17. ATM with Account Type
# First ask for account type:

# 1 → Savings
# 2 → Current
# Then show:

# 1 → Check Balance
# 2 → Deposit
# 3 → Withdraw
# Use nested match-case to display the selected account and operation.

# Sample Input
# Enter account type: 1
# Enter operation: 3
# Sample Output
# Savings Account
# Withdraw Selected
account_type = int(input("Enter account type: "))

match account_type:
    case 1:
        print("Savings Account")
        operation = int(input("Enter operation: "))

        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid operation")

    case 2:
        print("Current Account")
        operation = int(input("Enter operation: "))

        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid operation")

    case _:
        print("Invalid account type")

