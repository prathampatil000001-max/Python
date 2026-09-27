# 15. Matrix Value Analyzer
# Take a 3 × 3 matrix using nested for loops.

# For every number:

# Identify even/odd.
# Identify positive/negative/zero.
# At the end, print:

# Even count
# Odd count
# Positive count
# Negative count
# Zero count
# Largest number
# Do not use max().



matrix = []

even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0
zero_count = 0


for i in range(3):
    row = []

    for j in range(3):
        num = int(input(f"Enter value [{i}][{j}]: "))
        row.append(num)

        
        if num % 2 == 0:
            even_count += 1
            even_odd = "Even"
        else:
            odd_count += 1
            even_odd = "Odd"

        
        if num > 0:
            positive_count += 1
            sign = "Positive"
        elif num < 0:
            negative_count += 1
            sign = "Negative"
        else:
            zero_count += 1
            sign = "Zero"

        print(num, "->", even_odd, ",", sign)

    matrix.append(row)


largest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

print("\n----- Results -----")
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Positive count:", positive_count)
print("Negative count:", negative_count)
print("Zero count:", zero_count)
print("Largest number:", largest)
