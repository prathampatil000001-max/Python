#Question no.25


amount = float(input("Enter purchase amount: "))

if amount < 500:
    discount_percent = 0
elif amount < 1000:
    discount_percent = 5
elif amount < 2000:
    discount_percent = 10
elif amount < 5000:
    discount_percent = 15
else:
    discount_percent = 20

discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount

print("Original Amount = ₹", amount)
print("Discount Percentage =", discount_percent, "%")
print("Discount Amount = ₹", discount_amount)
print("Final Amount = ₹", final_amount)
