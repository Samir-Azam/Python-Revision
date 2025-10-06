"""
=======================================
   Python Conditionals & Match-Case
=======================================

This file contains revision notes and
examples for conditionals in Python.
"""

# -------------------------------
# ✅ if, elif, else
# -------------------------------

age = 18

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# -------------------------------
# ✅ Nested if
# -------------------------------

number = 12

if number > 0:
    if number % 2 == 0:
        print("Positive even number.")
    else:
        print("Positive odd number.")
else:
    print("Zero or negative number.")

# -------------------------------
# ✅ Ternary Expression (shorthand if-else)
# -------------------------------

marks = 85
result = "Pass" if marks >= 40 else "Fail"
print("Result:", result)

# -------------------------------
# ✅ Logical Operators in Conditionals
# -------------------------------

temperature = 25
if temperature > 20 and temperature < 30:
    print("Weather is pleasant.")

# -------------------------------
# ✅ match-case (Python 3.10+)
# -------------------------------

"""
match-case is similar to switch-case in other languages.
"""

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

# -------------------------------
# ✅ match-case with patterns
# -------------------------------

command = ("move", 10)

match command:
    case ("move", steps):
        print(f"Moving {steps} steps forward.")
    case ("turn", direction):
        print(f"Turning {direction}.")
    case _:
        print("Unknown command.")
