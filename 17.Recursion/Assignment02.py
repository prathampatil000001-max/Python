# Intermediate Recursion Assignments (Python)
# Instructions: Solve each problem using recursion. Do not use loops, lists, tuples, sets, dictionaries, or other data structures. Use only numbers, strings, function calls, and basic conditions.

# 1. Sum of Digits at Even Positions
# Write a recursive function that accepts a positive integer and returns the sum of the digits at even positions, counting positions from the rightmost digit as position 1.

# Example:
# Input: 583246
# Output: 12
# (The digits at even positions from the right are 4, 2, and 8.)

def sum_even(n):
    if n == 0:
        return 0

    return (n // 10 % 10) + sum_even(n // 100)


num = 583246
print(sum_even(num))

# 2. Reverse a Number Without Converting It to a String
# Write a recursive function that accepts a positive integer and returns the number with its digits in reverse order. Do not convert the number into a string.

# Example:
# Input: 4827
# Output: 7284

def reverse(n, rev=0):
    if n == 0:
        return rev

    return reverse(n // 10, rev * 10 + n % 10)
num = 4827
print(reverse(num))

