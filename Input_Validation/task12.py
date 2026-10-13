# Problem 12: Deposit Validation
# Start with a balance of ₹2,000. Ask the user for a deposit amount. Accept only positive amounts. Keep asking until a valid amount is entered, then add it to the balance and display the new balance.
balance = 2000

while True:
    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance = balance + amount
        print("Deposit successful!")
        print("New balance: ₹", balance)
        break
    else:
        print("Invalid amount! Please enter a positive amount.")