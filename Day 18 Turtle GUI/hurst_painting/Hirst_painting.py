import turtle
import random

# Predefined list of colors
color = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
         (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
         (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
         (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
         (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

hien = turtle.Turtle()
hien.speed("fastest")  # Set turtle speed to fastest
turtle.colormode(255)  # Set color mode to 255 for RGB values

# Move to starting position
hien.penup()
hien.setheading(225)
hien.forward(300)
hien.setheading(0)
# Hide the turtle
hien.hideturtle()

# Draw 10x10 grid of dots
for row in range(10):
    for _ in range(10):
        hien.dot(20, random.choice(color))
        hien.forward(50)

    # Move to the next row
    hien.backward(500)  # Go back to the start of the row
    hien.setheading(90)
    hien.forward(50)
    hien.setheading(0)

# finish
turtle.done()