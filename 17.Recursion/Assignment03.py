# 1. Print a Message N Times
# Write a recursive function that accepts a message and a positive integer n. Print the message exactly n times.

# Example:

# Input: message = "Hello", n = 3
# Output:
# Hello
# Hello
# Hello
# Hello         
def print_message(message, n):
    if n == 0:
        return
    print(message)
    print_message(message, n - 1)
print_message("Hello", 3)


# 2. Print Even Numbers from 2 to N
# Write a recursive function that accepts a positive integer n and prints all even numbers from 2 up to n.

    # Example:

# Input: n = 10
# Output: 2 4 6 8 10
def print_even(n):
    if n < 2:
        return

    print_even(n - 2)
    print(n, end=" ")

print_even(10)

# 3. Find the Sum of Odd Numbers from 1 to N
# Write a recursive function that accepts a positive integer n and returns the sum of all odd numbers from 1 to n.

# Example:

# Input: n = 7
# Output: 16
def sum_odd(n):
    if n <= 0:
        return 0

    if n % 2 == 1:
        return n + sum_odd(n - 2)
    else:
        return sum_odd(n - 1)
print(sum_odd(7))

# 4. Count How Many Times a Digit Appears
# Write a recursive function that accepts a non-negative integer number and a digit target. Return how many times the target digit appears in the number.

# Do not convert the number into a string.

# Example:

# Input: number = 52525, target = 5
# Output: 3








# 5. Find the Product of Digits
# Write a recursive function that accepts a non-negative integer and returns the product of its digits.

# Example:

# Input: 234
# Output: 24
def product_of_digits(n):
    if n == 0:
        return 1

    return (n % 10) * product_of_digits(n // 10)
print(product_of_digits(234))

# 6. Find the First Digit of a Number
# Write a recursive function that accepts a non-negative integer and returns its first (leftmost) digit.

# Do not convert the number into a string.

# Example:

# Input: 5837
# Output: 5
def first_digit(n):
    if n < 10:
        return n

    return first_digit(n // 10)
print(first_digit(5837))


# 7. Check Whether a Number Contains a Digit
# Write a recursive function that accepts a non-negative integer number and a digit target. Return True if the target digit appears in the number. Otherwise, return False.

# Do not convert the number into a string.

# Example:

# Input: number = 4826, target = 8
# Output: True
def contains_digit(number, target):
    if number == 0:
        return False
    if number % 10 == target:
        return True
    return contains_digit(number // 10, target)















