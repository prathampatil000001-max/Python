# Topic 6 — match-case with Simple Calculations
# Q20. Simple Calculator
# Take two numbers and an operator:

# +
# -
# *
# /
# Use match-case to perform the selected operation.

# Sample Input
# Enter first number: 20
# Enter second number: 5
# Enter operator: *
# Sample Output
# Result = 100
# Important
# Handle division separately and avoid division by zero.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        result = num1 + num2
        print("Result =", result)

    case "-":
        result = num1 - num2
        print("Result =", result)

    case "*":
        result = num1 * num2
        print("Result =", result)

    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result =", result)

    case _:
        print("Invalid operator")
