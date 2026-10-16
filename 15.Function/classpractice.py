
# Q]01
# def addition():
#     a=int(input("Enter a first number :-"))
#     b=int(input("Enter a second number :-"))
#     print(a+b)
# addition()

# Q]02
# def print_line():
#     print("--------------------")

# print("Student Report")
# print_line()
# print("Name: Asha")
# print_line()
# print("Marks: 85")
# print_line()


# def print_heading():
#     print("STUDENT REPORT")
#     print("----------------")

# def print_student_details():
#     print("Name: Asha")
#     print("Roll number: 12")

# def print_result():
#     print("Marks: 85")
#     print("Result: Pass")

# print_heading()
# print_student_details()
# print_result()



# def addition():
#     a=int(input("Enter a first number :-"))
#     b=int(input("Enter a second number :-"))
#     print(a+b)
# addition()

# def subtraction():
#     a=int(input("Enter a first number :-"))
#     b=int(input("Enter a second number :-"))
#     print(a-b)
# subtraction()

# def multiplication():
#     a=int(input("Enter a first number :-"))
#     b=int(input("Enter a second number :-"))
#     print(a*b)
# multiplication()

# def floordivision():
#     a=int(input("Enter a first number :-"))
#     b=int(input("Enter a second number :-"))
#     print(a//b)
# floordivision()

# # Q]03
# def even_odd():
#     num=int(input("Enter a number :"))
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# even_odd()

# def prinnting_number(number):
#     print(number)

# prinnting_number(100)
# prinnting_number(777)

# def subtract(a, b):
#     print(a - b)

# subtract(10, 3)

# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)

# def add(a, b):
#     print(a + b)

# answer = add(2, 3)
# print("Answer:", answer)

# def add(a, b):
#     return a + b

# answer = add(2, 3)
# print("Answer:", answer)
def add(a,b):
    c=a+b

result=add(10,20)
print(result)

def double(number):
    return number *2
def add_eight(number):
    return number + 8
result = add_eight(double(10))
print(result)

def calculate(a,b):
    total=a+b
    diffrence=a-b
    print(total,diffrence)

calculate (10, 4)

# 3. Default and Keyword Arguments
# 3.1 Default Arguments
# A default argument is a parameter value provided in the function definition. Python uses it when the caller does not supply an argument for that parameter.
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Asha")

def calculate(number):
    return number * 2

result = calculate(5)
print(result + 3)

def greet(name="Guest"):
    return "Hello " + name

print(greet())
print(greet("Asha"))
def values():
    return 10, 20

a, b = values()
print(a + b)
def show(a, b=5):
    print(a, b)

show(10)
show(10, 20)
show(a=7, b=3)
def demo():
    print("A")
    return 5
    print("B")

print(demo())

def total(a, b, c=10):
    return a + b + c

print(total(1, c=3, b=2))


