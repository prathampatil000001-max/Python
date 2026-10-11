# Q8. Divisible by 3 and 5
# Given a number, print if it is divisible by both 3 and 5.

# Input: 15 → Output: "divisible by 3 and 5"
# Input: 30 → Output: "divisible by 3 and 5"
# Input: 9 → Output: "not divisible by both"
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("divisible by 3 and 5")
else:
    print("not divisible by both")