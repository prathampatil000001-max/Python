# Questions
# 1. Add Two Numbers
# Create a lambda function that accepts two numbers and returns their sum.

# Sample values: 10, 20
# Expected output: 30
add_two_numbers = lambda x, y: x + y
print(add_two_numbers(10, 20))


# 2. Find the Square
# Create a lambda function that accepts one number and returns its square.

# Sample value: 6
# Expected output: 36
find_square = lambda x: x ** 2
print(find_square(6))


# 3. Find the Cube
# # Create a lambda function that accepts one number and returns its cube.

# Sample value: 3
# Expected output: 27

find_cube = lambda x: x ** 3
print(find_cube(3))


# 4. Check Even or Odd
# Create a lambda function that accepts one number and returns "Even" if the number is even, and "Odd" if the number is odd.
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_odd(10))  
print(check_even_odd(7)) 

# 5. Find the Greater Number
# Create a lambda function that accepts two numbers and returns the greater number.

# Sample values: 45, 32
# Expected output: 45

find_greater = lambda x, y: x if x > y else y
print(find_greater(45, 32))

# 6. Convert Celsius to Fahrenheit
# Create a lambda function that accepts a temperature in Celsius and converts it to Fahrenheit.

# Use this formula:

# Fahrenheit = (Celsius * 9/5) + 32

# Sample value: 25
# Expected output: 77.0

convert_celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(convert_celsius_to_fahrenheit(25))

# 7. Calculate the Length of a String
# Create a lambda function that accepts a string and returns the number of characters in it.

# Sample value: "Python"
# Expected output: 6

calculate_length = lambda s: len(s)
print(calculate_length("Python"))

# 8. Convert a String to Uppercase
# Create a lambda function that accepts a string and returns the string in uppercase.

# Sample value: "hello world"
# Expected output: "HELLO WORLD"

convert_to_uppercase = lambda s: s.upper()
print(convert_to_uppercase("hello world"))

# 9. Find the Last Character
# Create a lambda function that accepts a non-empty string and returns its last character.

# Sample value: "Coding"
# Expected output: "g"

find_last_character = lambda s: s[-1]
print(find_last_character("Coding"))


# 0. Calculate the Final Price
# Create a lambda function that accepts the original price and discount percentage. Return the final price after applying the discount.

# Formula:

# Final Price = Original Price - (Original Price * Discount / 100)

# Sample values: Original price = 1000, Discount = 10
# Expected output: 900.0
calculate_final_price = lambda original_price, discount: original_price - (original_price * discount / 100)
print(calculate_final_price(1000, 10))