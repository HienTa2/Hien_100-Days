# function with input

# def greet():
#     print("Hello")
#     print("How do you do?")
#
#
# greet()
#
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# client = input("What is your name?")
#
# greet_with_name(client)

# function with 2 parameters
# def greet_with(name, location):
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}?")
#
#
# # argument
# greet_with("Hien", "Texas")
#
#
# # keyword argument
# greet_with(name="Hien", location="Texas")
#
#
# # *args and **kwargs.
# def func(*args):
#     for arg in args:
#         print(arg)
#
#
# func(1, 2, 3, 4)  # Outputs: 1 2 3 4
#
#
# def func(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")
#
#
# func(a=1, b=2, c=3)  # Outputs: a = 1, b = 2, c = 3

# Challenge
import math


# Write your code below this line 👇
def paint_calc(height, width, cover):
    area = height * width
    num_of_can = math.ceil(area / cover)
    print(f"You'll need {num_of_can} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
