# Section A — Understand Recursion (10 marks)
# 1. Predict the output (2 marks)
def show(n):
    if n == 0:
        print("Stop")
        return

    print(n)
    show(n - 1)
    print(n)

show(2)
# OUTPUT:-Stop
    #    2
    #    1


# 2. Find the base case (2 marks)
# In this function, identify the base case and explain why it stops recursion.
def total(n):
    if n == 0:
        return 0

    return n + total(n - 1)

# OUTPUT:-1
        # 2


# 3. Find the bug (3 marks)
# Explain why this function does not reach its base case when called with count(2). Rewrite the incorrect line.

def count(n):
    if n == 0:
        return

    count(n - 1) 
count(2)


# 4. Print or return? (3 marks)
# What does this function return when called as answer(3)? Explain why.

# def answer(n):
#     if n == 0:
#         return 0

#     n + answer(n - 1)

# print(answer(3))

# OUTPUT:-NONE and TypeEror
# Explanation:-
# answer(3) calls answer(2).

# answer(2) calls answer(1).

# answer(1) calls answer(0).

# answer(0) returns 0.



# ////////////////////======================================////////////////////////////////////////////////////////////


# 5.]] Count down (4 marks)
# Write countdown(n) that prints every integer from n down to 1, then prints "Done!".

# Constraint: n is a non-negative integer.

# Examples:

# countdown(3)
# Output:

# 3
# 2
# 1
# Done!
# Edge case: countdown(0) should print only Done!.

def count_down(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    count_down(n -1)

count_down(3)

# /////////////////////------------------------------------------------------//////////////////////////////////////

# 6. Count up (4 marks)
# Write count_up(n) that prints numbers from 1 through n in ascending order.

# Example:

# count_up(4)
# Output:

# 1
# 2
# 3
# 4
# Edge case: count_up(0) should print nothing.
def count_up(n):
    if n==1:
        print(1)
        return
    count_up(n-1)
    print(n)
count_up(4)




# 7. Sum from 1 to n (4 marks)
# Write sum_to(n) that returns the sum of all integers from 1 through n.

# Examples:

# print(sum_to(5))  # 15
# print(sum_to(0))  # 0
# Constraint: n is a non-negative integer.

def sum_to(n):
    return n * (n + 1) // 2


print(sum_to(5))  
print(sum_to(0))  

# 8. Factorial (4 marks)
# Write factorial(n) that returns n!.

# Examples:

# print(factorial(4))  # 24
# print(factorial(0))  # 1
# Constraint: n is a non-negative integer.
# Constraint: n is a non-negative integer
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(4))  # 24
print(factorial(0))  # 1


# 9. Sum of digits (4 marks)
# Write digit_sum(n) that returns the sum of the digits of a non-negative integer.

# Examples:

# print(digit_sum(583))  # 16
# print(digit_sum(7))    # 7
# print(digit_sum(0))    # 0
# Hint: % 10 gets the last digit; // 10 removes the last digit.

def sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(sum(583)) 
print(sum(7))
print(sum(0))    
    
# 10. Power (5 marks)
# Write power(base, exponent) that returns base raised to exponent.

# Examples:

# print(power(2, 5))  # 32
# print(power(9, 0))  # 1
# print(power(3, 1))  # 3
# Constraint: exponent is a non-negative integer. Do not use ** in your function.
def  power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
print(power(2,3))

# ________________
# _____Question-11______
def count_digits(n):
    if -10 < n < 10:
        return 1

    return 1 + count_digits((n-1) // 10)
print(count_digits(0))

# ________________
# _____Question-12______
def reverse_text(n):
    if n == "":
        return ""
    return reverse_text(n[1:])+n[0]
print(reverse_text("qwe"))

# ________________
# _____Question-13______
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# ________________
# _____Question-14______
def max_digit(n):
    if n == 0:
        return 0
    num1 = n % 10
    num2 = max_digit(n // 10)

    if num1 > num2:
        return num1
    else:
        return num2
print(max_digit(4729))  # 9
print(max_digit(555))   # 5
print(max_digit(0))     # 0

# ________________
# _____Question-15______
def mystery(n):
    if n <= 1:
        return n

    return mystery(n - 1) + mystery(n - 2)
print(mystery(4))
print(mystery(0))
print(mystery(1))
print(mystery(2))

# ________________
# _____Question-16______
def factorial(n):
    if n == 0:
        return 1# return 0 
    
    return n * factorial(n - 1)
print(factorial(5))

# ________________
# _____Question-17______
def stop_at_zero(n):
    if n == 0:
        return
    print(n)
    return stop_at_zero(n-1)
stop_at_zero(7)

# ________________
# _____Question-18______
# If a recursive function makes too many nested calls then  Python may have reached its recursion limit and after that it will give a Recursive Error.