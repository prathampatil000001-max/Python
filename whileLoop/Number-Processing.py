# number = 472

# while number > 0:
#     digit = number % 10
#     print(digit)
#     number = number // 10
# Print numbers from 1 to 10, but stop when the number becomes 6.
for i in range(1, 10):
    print(i)
    if i == 6:
        break
#     Problem 2
# Given:

# numbers = [10, 20, 30, 40, 50]
# Search for 30.

# Once found, print:

# Found
# and stop the loop.
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Found")
        break
# Problem 3
# Take numbers from the user continuously.

# Stop when the user enters 0.
while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break
# Problem 4
# Print numbers from 1 to 100, but stop when you reach the first number divisible by 17.

for i in range(1, 101):
    if i % 17 == 0:
        break
    print(i)