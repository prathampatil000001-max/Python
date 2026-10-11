# Level 1 – Basics (numbers, variables, if-else)
# Q1. Even or Odd
# Given a number, print whether it is "even" or "odd".

# Input: 4 → Output: "even"
# Input: 7 → Output: "odd"
# Input: 0 → Output: "even"
n = int(input())

if n % 2 == 0:
    print("even")
else:
    print("odd")