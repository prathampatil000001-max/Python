# 9. Practice Questions
# Try solving these without looking at the examples above.

# 01] Write multiply_all(*args) that returns the product of all supplied numbers. Decide what it should return when no numbers are supplied.
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_all(2, 3, 4))  # 24
print(multiply_all(5, 6))     # 30
print(multiply_all(7))        # 7
print(multiply_all())      # 1

# 02] Write print_profile(**kwargs) that prints each key and value on a separate line.
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
print_profile(name="Rahul", age=21, city="Pune")

# 03] Define make_message(name, /, *, greeting="Hello"). Call it using valid and invalid argument styles.
def make_message(name, /, *, greeting="Hello"):
    return f"{greeting}, {name}!"
print(make_message("Rahul"))
# Hello, Rahul!

print(make_message("Rahul", greeting="Hi"))
# Hi, Rahul!

print(make_message("Priya", greeting="Welcome"))
# Welcome, Priya!

#04] Given values = [4, 5, 6], call a three-parameter function by unpacking values.
def add_three(a, b, c):
    return a + b + c

values = [4, 5, 6]

print(add_three(*values))
# 15

# 05] Given person = {"name": "Ravi", "age": 21}, unpack it into a function with matching parameters.
def print_person(name, age):
    print("Name:", name)
    print("Age:", age)

person = {"name": "Ravi", "age": 21}

print_person(**person)
# Name: Ravi
# Age: 21

# 06] Write a function with a docstring that explains its purpose, parameters, and return value.
def add_numbers(a, b):
    """
    Add two numbers together.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


print(add_numbers(10, 20))
# 30

# 07] Add parameter and return type hints to a function that calculates a rectangle's area.
def rectangle_area(length, width):
    return length * width


print(rectangle_area(5.0, 3.0))

# 15.0

# 08] Explain why type hints alone do not prevent a function from receiving a value of the wrong type.
def rectangle_area(length: float, width: float) -> float:
    return length * width

print(rectangle_area("5", 3))

# 09] What happens if the same parameter gets a value both positionally and through **kwargs?
def greet(name):
    print("Hello", name)

details = {"name": "Ravi"}

greet("Amit", **details)

# 10] Explain the difference between *args in a function definition and *values in a function call.
def add_three(a, b, c):
    return a + b + c

values = [2, 3, 4]

print(add_three(*values))
