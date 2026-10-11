# Q6. Grade Calculator
# Given marks 0–100, print grade.

# Example mapping:

# 90–100 → A

# 80–89 → B

# 70–79 → C

# 60–69 → D

# 0–59 → F

# Input: marks = 92 → Output: "A"

# Input: marks = 75 → Output: "C"

# Input: marks = 40 → Output: "F"
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")