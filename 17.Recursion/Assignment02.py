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

# 3. Check Whether a String Is a Palindrome
# Write a recursive function that accepts a string and returns whether it reads the same forward and backward. The function must compare characters recursively without using loops or slicing.

# Example:
# Input: level
# Output: True

def is_palindrome(s, start=0, end=None):
    if end is None:
        end = len(s) - 1

    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return is_palindrome(s, start + 1, end - 1)

word = "level"
print(is_palindrome(word))


# 4. Count a Character in a String
# Write a recursive function that accepts a string and a character. Return how many times that character appears in the string. Treat uppercase and lowercase characters as different.

# Example:
# Input: programming, m
# Output: 2
def count_character(s, ch):
    if len(s) == 0:
        return 0

    if s[0] == ch:
        return 1 + count_character(s[1:], ch)
    else:
        return count_character(s[1:], ch)

word = "programming"
char = "m"

print(count_character(word, char))

# 5. Find the Greatest Common Divisor
# Write a recursive function that accepts two positive integers and returns their greatest common divisor (GCD). Do not use built-in GCD functions.

# Example:
# Input: 48, 18
# Output: 6

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)
num1 = 48
num2 = 18
print(gcd(num1, num2))

# 6. Check Whether a Number Is a Prime Number
# Write a recursive function that accepts an integer greater than 1 and checks whether it is prime. Use recursion to test possible divisors. Do not use loops.

# Example:
# Input: 29
# Output: True
def is_prime(n, divisor=2):
    if divisor == n:
        return True

    if n % divisor == 0:
        return False

    return is_prime(n, divisor + 1)
num = 29
print(is_prime(num))
# 7. Remove All Occurrences of a Character
# Write a recursive function that accepts a string and a character. Return a new string with every occurrence of that character removed. Do not use the built-in replace() method.

# Example:
# Input: mississippi, s
# Output: miippi
def remove_character(s, ch):
    if len(s) == 0:
        return ""

    if s[0] == ch:
        return remove_character(s[1:], ch)

    return s[0] + remove_character(s[1:], ch)
word = "mississippi"
char = "s"
print(remove_character(word, char))
# 8. Convert a Decimal Number to Binary
# Write a recursive function that accepts a non-negative decimal integer and returns its binary representation as a string. Do not use bin().

# Example:
# Input: 13
# Output: 1101
def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return decimal_to_binary(n // 2) + str(n % 2)
num = 13
print(decimal_to_binary(num))

# 9. Check Whether a String Contains Only Digits
# Write a recursive function that accepts a non-empty string and checks whether every character is a digit from 0 to 9. Do not use loops or the built-in isdigit() method.

# Example:
# Input: 50291
# Output: True
def only_digits(s):
    if len(s) == 0:
        return True

    if s[0] < '0' or s[0] > '9':
        return False

    return only_digits(s[1:])
word = "50291"
print(only_digits(word))

# 10. Find the Digital Root
# Write a recursive function that accepts a positive integer and repeatedly adds its digits until only one digit remains. Return that final digit.

# Example:
# Input: 9875
# Output: 2
# (First: 9 + 8 + 7 + 5 = 29; then: 2 + 9 = 11; then: 1 + 1 = 2.)
def sum_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)
def digital_root(n):
    if n < 10:
        return n

    return digital_root(sum_digits(n))
num = 9875
print(digital_root(num))