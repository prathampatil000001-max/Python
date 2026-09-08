#Question no .22

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check whether the sides form a valid triangle
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")

# Determine triangle type
elif a == b == c:
    print("Equilateral")

elif a == b or b == c or a == c:
    print("Isosceles")

else:
    print("Scalene")
