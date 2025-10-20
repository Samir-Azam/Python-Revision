# decorators are basically a wrapper around a function
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print(f"Start executing {func.__name__}")
        func()
        print(f"Execution of {func.__name__} is completed")

    return wrapper

@my_decorator
def printHelloWorld():
    print("Hello World")

printHelloWorld()
print(printHelloWorld.__name__)