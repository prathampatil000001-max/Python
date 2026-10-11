# Q4. Positive, Negative, or Zero
# Given a number, print "positive", "negative", or "zero".

# Input: 8 → Output: "positive"
# Input: -2 → Output: "negative"
# Input: 0 → Output: "zero"
n = int(input())

if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
