# Q5. Age Group
# Given an age, print whether the person is "child", "teenager", or "adult" (you can assume: 0–12 child, 13–19 teenager, 20+ adult).

# Input: age = 8 → Output: "child"
# Input: age = 15 → Output: "teenager"
# Input: age = 25 → Output: "adult"
age = int(input("Enter age: "))

if age <= 12:
    print("child")
elif age <= 19:
    print("teenager")
else:
    print("adult")