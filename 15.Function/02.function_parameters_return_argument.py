# 5. Dry-Run Questions
# Predict the output before running each program.

# Question 1
def greet(name):
    print("Hello", name)

greet("Asha")
greet("Rahul")
# Hello Asha
# Hello Rahul

# Question 2
def subtract(a, b):
    return a - b

print(subtract(8, 3))
print(subtract(3, 8))
# 5
# -5

# Question 3
def calculate(number):
    return number * 2

result = calculate(5)
print(result + 3)
# 13

# Question 4
def greet(name="Guest"):
    return "Hello " + name

print(greet())
print(greet("Asha"))
# Hello Guest
# Hello Asha

# Question 5
def values():
    return 10, 20

a, b = values()
print(a + b)
# 30//

# Question 6
def show(a, b=5):
    print(a, b)

show(10)
show(10, 20)
show(a=7, b=3)
# 10 5
# 10 20
# 7 3

# Question 7
def demo():
    print("A")
    return 5
    print("B")

print(demo())
# A
# 5

# Question 8
def total(a, b, c=10):
    return a + b + c

print(total(1, c=3, b=2))
# 6

# 6. Practice Problems
# Try solving these without looking at the solutions first.

# Beginner

#01] Define a function named welcome that prints Welcome to Python. Call it three times.
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()

# 02] Define greet(name) that prints a greeting using the given name.
def greet(name):
    print("Hello,", name)

greet("Rahul")

#03] Define show_number(number) that prints the number passed to it.
def show_number(number):
    print(number)
show_number(10)

# 04] Define add(a, b) that returns the sum of two numbers
def add(a, b):
    return a + b
print(add(3, 5))

# 05 Define square(number) that returns the square of a number.
def square(number):
    return number ** 2

# Example
def square(number):
    return number ** 2
print(square(5)) 


# 6. Practice Problems
# Try solving these without looking at the solutions first.

# Beginner
# 01] Define a function named welcome that prints Welcome to Python. Call it three times.
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()


# 02] Define greet(name) that prints a greeting using the given name.
def greet(name):
    print("Hello,", name)

greet("Alice")

# 03] Define show_number(number) that prints the number passed to it.
def show_number(number):
    print(number)

show_number(10)

# 04] Define add(a, b) that returns the sum of two numbers.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# 05] Define square(number) that returns the square of a number.
def square(number):
    return number * number

result = square(5)
print(result)

# 06] Define is_even(number) that returns True if the number is even and False otherwise.
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))

# 07] Define get_full_name(first_name, last_name) that returns the full name.
def get_full_name(first_name, last_name):
    return first_name + " " + last_name

result = get_full_name("Rahul", "Sharma")
print(result)

# 08] Define introduce(name, city="Pune") and test it with and without a city argument.
def introduce(name, city="Pune"):
    print("My name is", name, "and I live in", city)

introduce("Rahul")

introduce("Priya", "Mumbai")

# 09] Define subtract(a, b) and show how changing positional argument order changes the result.
def subtract(a, b):
    return a - b

print(subtract(10, 3))
print(subtract(3, 10))

# 10] Define get_min_max(a, b) that returns both the smaller and larger values.
def get_min_max(a, b):
    return min(a, b), max(a, b)

result = get_min_max(10, 5)
print(result)

# 11]Define calculate(a, b) that returns the sum, difference, product, and quotient. Assume b is not zero.
def calculate(a, b):
    return a + b, a - b, a * b, a / b

sum_result, difference, product, quotient = calculate(10, 2)

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# 12] Define count_digits(number) that returns the number of digits in a non-negative integer. For this exercise, treat 0 as having one digit.
def count_digits(number):
    return len(str(number))

print(count_digits(12345))
print(count_digits(7))
print(count_digits(0))

# 13] Define classify_number(number) that returns "Positive", "Negative", or "Zero".
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(classify_number(10))
print(classify_number(-5))
print(classify_number(0))

# 14] Define calculate_total(price, quantity=1) that returns the total price.
def calculate_total(price, quantity=1):
    return price * quantity

print(calculate_total(100))
print(calculate_total(100, 3))

# 15] Define create_email(username, domain="example.com") that returns an email address.
def create_email(username, domain="example.com"):
    return username + "@" + domain

print(create_email("rahul"))
print(create_email("priya", "gmail.com"))

# 16] Define format_name(first, last, uppercase=False). If uppercase is True, return the full name in uppercase.
def format_name(first, last, uppercase=False):
    full_name = first + " " + last

    if uppercase:
        return full_name.upper()
    else:
        return full_name

print(format_name("Rahul", "Sharma"))
print(format_name("Rahul", "Sharma", True))

# 17] Define percentage(marks, total=100) that returns the percentage. Assume total is not zero.
def percentage(marks, total=100):
    return (marks / total) * 100

print(percentage(85))
print(percentage(45, 50))

# 18] Define convert_minutes(minutes, seconds_per_minute=60) that returns the total seconds.
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

print(convert_minutes(5))
print(convert_minutes(2, 60))

# 19] Define student_details(name, age, city) and call it using keyword arguments in a different order.
def student_details(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student_details(city="Pune", name="Rahul", age=20)

# 20] Define bill(item, quantity=1, price=100) that returns the bill amount. Test positional and keyword calls
def bill(item, quantity=1, price=100):
    return quantity * price

print(bill("Pen"))
print(bill("Book", 3, 50))

print(bill(item="Pencil", quantity=5, price=10))
print(bill(item="Notebook", price=80))

# Challenging
# 21] Define analyze_number(number) that returns three values: the absolute value, whether it is even, and the number of digits. Do not use abs(); assume the input is an integer.
def analyze_number(number):
    
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number

    is_even = number % 2 == 0

    digits = len(str(absolute_value))

    return absolute_value, is_even, digits

print(analyze_number(-246))
print(analyze_number(135))
print(analyze_number(0))

# 22] Define calculate_stats(a, b, c) that returns the smallest, largest, and sum of three numbers.
def calculate_stats(a, b, c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    total = a + b + c

    return smallest, largest, total

print(calculate_stats(10, 5, 20))

# 23] Define make_sentence(subject, verb, object) that returns a sentence. Call it with keyword arguments in a different order.

def make_sentence(subject, verb, object):
    return subject + " " + verb + " " + object + "."

sentence = make_sentence(object="Python", subject="I", verb="love")
print(sentence)

# 24] Define apply_discount(price, discount=0) that returns the final price after subtracting the discount percentage. Assume discount is between 0 and 100.
def apply_discount(price, discount=0):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price

print(apply_discount(1000))
print(apply_discount(1000, 20))
print(apply_discount(500, 10))

# 25] Define calculate_pay(hours, rate=200, bonus=0) that returns hours * rate + bonus. Try different combinations of positional and keyword arguments.
def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus

print(calculate_pay(8))

print(calculate_pay(8, 250))

print(calculate_pay(8, 250, 500))

print(calculate_pay(hours=8, rate=250, bonus=500))

print(calculate_pay(8, bonus=300))

print(calculate_pay(hours=6, bonus=200))

# Define get_coordinates(x=0, y=0) that returns both values. Test default calls and calls with only one keyword argument.
def get_coordinates(x=0, y=0):
    return x, y

print(get_coordinates())

print(get_coordinates(x=5))

print(get_coordinates(y=8))

print(get_coordinates(x=3, y=4))

# 27] Define compare(a, b) that returns two values: "A is greater", "B is greater", or "Equal" as the first value, and the absolute difference as the second value. Do not use abs().
def compare(a, b):
    if a > b:
        message = "A is greater"
        difference = a - b
    elif b > a:
        message = "B is greater"
        difference = b - a
    else:
        message = "Equal"
        difference = 0

    return message, difference


print(compare(10, 5))
print(compare(3, 8))
print(compare(6, 6))

# 28] Define convert_temperature(value, scale="C"). If scale is "C", convert Celsius to Fahrenheit; if "F", convert Fahrenheit to Celsius. Return the converted value. Assume the scale is valid.

def convert_temperature(value, scale="C"):
    if scale == "C":
        return (value * 9 / 5) + 32
    else:
        return (value - 32) * 5 / 9


print(convert_temperature(25))
print(convert_temperature(77, "F"))
print(convert_temperature(0, "C"))

#29] Define calculate_result(marks, passing_marks=35) that returns "Pass" if marks meet the passing mark and "Fail" otherwise.
def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"

print(calculate_result(70))
print(calculate_result(30))
print(calculate_result(40, 50))
print(calculate_result(35))

# # Define order_summary(item, quantity=1, price=100, delivery_fee=40) that returns the total cost. Use keyword arguments to change only the delivery fee.
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return quantity * price + delivery_fee

# print(order_summary("Book"))

# print(order_summary("Book", delivery_fee=20))

# def info(age,a,name="pp"):
#     print(a)
#     return 5
# a=info(name="sharan",age=20,a=30)
# print(a)
# print(info(name="sharan",age=20,a=30))

def info(a,b,c,e,f,g,k,*args):
    print(a,b,c) 
    print(args)
info(8,8,6,7,5,4,0,6,5)


# text = "call of duty"
# word = "duty"

# found = False

# for i in range(len(text) - len(word) + 1):
#     if text[i:i + len(word)] == word:
#         found = True
#         print("Found at index:", i)
#         break

# if not found:
#     print("Not found")

def devide(c,d,/,*,a,b):
    return a/b,c+d
print(devide(14,15,a=10,b=2))

def book_ticket(source, destination, /, *, passenger, seat="regular"):
    print(source, "to", destination)
    print("Passenger:", passenger)
    print("Seat:", seat)

book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
book_ticket("Pune", "Mumbai", passenger="Asha")

def add(**kwargs):
    print(kwargs)
    print(type(kwargs))
add()
add(a=10, b=20, c=30)



