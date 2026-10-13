# Problem 17: Banking Menu
# Create a menu-driven banking program with these options:

# 1. Check balance
# 2. Deposit money
# 3. Withdraw money
# 4. Exit
# Start with a balance of ₹10,000.

# Requirements:

# Keep displaying the menu until the user chooses Exit.
# Reject invalid menu choices.
# Deposits must be greater than zero.
# Withdrawals must be greater than zero and must not exceed the balance.
# Update the balance only after a transaction passes validation.
balance = 10000

while True:
    print("Banking Menu")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("Current balance: ₹", balance)

    elif choice == '2':
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
            print("Updated balance: ₹", balance)
        else:
            print("Invalid amount. Deposit must be greater than zero.")

    elif choice == '3':
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful.")
            print("Updated balance: ₹", balance)

    elif choice == '4':
        print("Thank you for using our banking service!")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 4.")