# Q7. Divisible by 5
# Given a number, print whether it is divisible by 5.

# Input: 10 → Output: "divisible by 5"
# Input: 11 → Output: "not divisible by 5"
# Input: 0 → Output: "divisible by 5"
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")