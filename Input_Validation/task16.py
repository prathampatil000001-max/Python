# Problem 16: Calculator Input Validation
# Build a calculator that asks for two numbers and an operator (+, -, *, or /).

# Validate the following:

# The operator must be one of the four supported operators.
# Division by zero must be rejected.
# If the operator is invalid, ask for the operator again.
# If the divisor is zero, ask for the second number again.
# Display the result only when all required values are valid
num1 = float(input("Enter the first number: "))

while True:
    operator = input("Enter an operator (+, -, *, /): ")
    if operator in ['+', '-', '*', '/']:
        break
    print("Invalid operator. Please try again.")

while True:
    num2 = float(input("Enter the second number: "))

    if operator == '/' and num2 == 0:
        print("Division by zero is not allowed. Enter again.")
    else:
        break

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
else:
    result = num1 / num2

print("Result:", result)