# Topic 7 — match-case + if
# Q23. ATM Withdrawal
# Create an ATM withdrawal program.

# First use match-case for:

# 1 → Savings
# 2 → Current
# For either account, ask for withdrawal amount.

# Use if to check:

# If amount is positive, continue.
# If amount is zero or negative, display Invalid Amount.
# Sample Input
# Enter account type: 1
# Enter amount: 500
# Sample Output
# Savings Account
# Withdrawal Request Accepted

account_type = int(input("Enter account type: "))

match account_type:
    case 1:
        print("Savings Account")
        amount = float(input("Enter amount: "))

        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case 2:
        print("Current Account")
        amount = float(input("Enter amount: "))

        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case _:
        print("Invalid Account Type")
