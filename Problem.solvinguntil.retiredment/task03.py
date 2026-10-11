# Q3. Maximum of Three Numbers
# Given three numbers, print the largest.

# Input: a = 3, b = 7, c = 5 → Output: 7
# Input: a = 10, b = 2, c = 10 → Output: 10
# Input: a = -1, b = -5, c = -3 → Output: -1
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)