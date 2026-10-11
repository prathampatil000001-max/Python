# Q10. In Range 10–50
# Given a number, check if it lies between 10 and 50 (inclusive).

# Input: 25 → Output: "in range"
# Input: 10 → Output: "in range"
# Input: 7 → Output: "out of range"
num = int(input("Enter a number: "))

if 10 <= num <= 50:
    print("in range")
else:
    print("out of range")