import time


def delay_decorator(function):
    time.sleep(2)

    def wrapper_function():
        function()

    return wrapper_function()


def say_hello():
    time.sleep(5)
    print("Hello")


decorator_function(say_hello)
say_hello()
