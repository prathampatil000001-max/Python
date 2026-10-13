# Problem 7: Withdrawal Validation
# Start with a bank balance of ₹5,000. Ask the user for a withdrawal amount. Reject the amount if it is zero, negative, or greater than the available balance. Keep asking until a valid amount is entered, then update and display the balance.
balance = 5000

while True:
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0 or amount > balance:
        print("Invalid amount! Please enter an amount greater than 0 and not more than your balance.")
    else:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance: ₹", balance)
        break