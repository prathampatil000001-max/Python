# 12. Practice Problems
# Beginner
# 01]Create a function with a local variable city and print it.
# 02]Create a global variable school. Read it inside a function.
# 03]Assign a variable inside an if block and print it outside the block.
# 04]Use a for loop to assign a loop variable. Print it after the loop.
# 05]Explain the difference between scope and lifetime in your own words.

# 01]
def test():
    city="pune"
    print(city)
test()

# 02]
school = "Sahakar Vidya Mandir  School"  

def display():
    print("School name:", school)

display()

# 03]
if True:
    x = 10

print("The value of x is:", x)


# 04]
for i in range(5):
    pass

print(i)
