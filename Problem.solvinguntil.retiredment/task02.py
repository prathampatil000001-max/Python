# Q2. Maximum of Two Numbers
# Given two numbers, print the larger one.

# Input: a = 5, b = 9 → Output: 9
# Input: a = 12, b = 3 → Output: 12
# Input: a = -4, b = -10 → Output: -4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
else:
    print(b)