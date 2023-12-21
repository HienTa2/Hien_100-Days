import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function  # Return the function itself


@delay_decorator
def say_hello():
    print("Hello")


def say_bye():
    print("Goodbye")


say_hello()  # This should now execute with a 2-second delay before printing "Hello"
say_bye()  # This should print "Goodbye" immediately after "Hello"
