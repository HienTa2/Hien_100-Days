import random
import turtle as t
from turtle import Turtle, Screen, done

Hien = Turtle()
Hien.shape("turtle")
Hien.color('red', 'green')

# Draw a square
# for _ in range(4):
#     Hien.forward(100)
#     Hien.right(90)

# Draw dotted line
# for _ in range(10):
#     Hien.forward(5)
#     Hien.penup()
#     Hien.forward(5)
#     Hien.pendown()

# Challenge need to draw 360 / 5 to get 72 degree

# def draw_shape(num_sides, color):
#     angle = 360 / num_sides
#     Hien.color(color)
#     for _ in range(num_sides):
#         Hien.forward(100)
#         Hien.right(angle)
#
#
# # Draw shapes from triangle to decagon
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'brown', 'pink', 'gray', 'cyan']
# for n in range(3, 11):
#     draw_shape(n, colors[n - 3])
#     Hien.penup()
#     Hien.setposition(0, 0)
#     Hien.pendown()


# Drawing a Spirograph
for _ in range(0, 100):
    Hien.speed('fastest')
    Hien.color(random.choice(colors))
    Hien.circle(100)
    current_heading = Hien.heading()
    Hien.setheading(current_heading + 10)


# To keep the window open
t.done()
