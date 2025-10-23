
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter first number: "))
    c = a/b
    print(f" {a} / {b} is {c}")
except ZeroDivisionError as e:
    print("Divisor can't be 'Zero'")
else:
    print("Program is executed successfully")
finally:
    print("This will get executed always")