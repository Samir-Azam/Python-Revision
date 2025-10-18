"""
📘 Python Functions Notes
This file contains explanations + code examples for Python functions.
You can run parts of it to see outputs.
"""

# -------------------------------------------------
# 1. What is a Function?
# -------------------------------------------------
# A function is a block of code that performs a specific task.
# Helps in code reusability, readability, and modularity.

# Example:
def greet():
    print("Hello, World!")

greet()


# -------------------------------------------------
# 2. Function with Parameters
# -------------------------------------------------
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Samir")


# -------------------------------------------------
# 3. Default Parameters
# -------------------------------------------------
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Samir")


# -------------------------------------------------
# 4. Return Statement
# -------------------------------------------------
def add(a, b):
    return a + b

print("Sum:", add(5, 10))


# -------------------------------------------------
# 5. Multiple Return Values
# -------------------------------------------------
def calculate(a, b):
    return a+b, a-b, a*b

s, d, m = calculate(10, 5)
print(s, d, m)


# -------------------------------------------------
# 6. Keyword & Positional Arguments
# -------------------------------------------------
def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

intro("Samir", 21)                 # Positional
intro(age=21, name="Samir")        # Keyword


# -------------------------------------------------
# 7. Arbitrary Arguments (*args and **kwargs)
# -------------------------------------------------
def numbers(*args):
    print("Numbers:", args)

numbers(1, 2, 3, 4)

def person(**kwargs):
    print("Person info:", kwargs)

person(name="Samir", age=21)


# -------------------------------------------------
# 8. Lambda (Anonymous Function)
# -------------------------------------------------
square = lambda x: x*x
print("Square of 5:", square(5))


# -------------------------------------------------
# 9. Nested Functions
# -------------------------------------------------
def outer():
    def inner():
        print("This is inner function")
    inner()

outer()


# -------------------------------------------------
# 10. Scope of Variables
# -------------------------------------------------
x = 10  # Global variable

def func():
    x = 5  # Local variable
    print("Local:", x)

func()
print("Global:", x)


# -------------------------------------------------
# 11. Recursion
# -------------------------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))


# -------------------------------------------------
# 12. map(), filter(), reduce() with Functions
# -------------------------------------------------
nums = [1, 2, 3, 4]

# map
squares = list(map(lambda x: x**2, nums))

# filter
evens = list(filter(lambda x: x%2==0, nums))

# reduce
from functools import reduce
product = reduce(lambda x, y: x*y, nums)

print("Squares:", squares)
print("Evens:", evens)
print("Product:", product)


# -------------------------------------------------
# ✅ Summary
# -------------------------------------------------
# - Functions help in modular coding.
# - Can have arguments, return values, and defaults.
# - Support recursion, lambdas, args/kwargs.
# - Used with map, filter, reduce for clean coding.
