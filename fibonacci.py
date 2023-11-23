import turtle as t
import math


# Define a function to draw a single Fibonacci square
def draw_fibonacci_square(turtle, side_length):
    """Draw a square of a given side length."""
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)


# Define a function to draw multiple Fibonacci squares based on the sequence
def draw_fibonacci_squares(turtle, number_of_squares):
    """Calculate and draw Fibonacci squares."""
    value_one, value_two = 0, 1
    for _ in range(number_of_squares):
        draw_fibonacci_square(turtle, value_two * 20)
        turtle.right(90)
        value_one, value_two = value_two, value_one + value_two


def draw_fibonacci_spiral(turtle, squares):
    """Draw a series of Fibonacci squares and arcs that approximate a spiral."""
    # Define initial values for the Fibonacci sequence
    a, b = 0, 1
    for i in range(squares):
        # Draw the square
        draw_fibonacci_square(turtle, b * 20)
        # Move the turtle to the start point of the arc
        turtle.penup()
        turtle.forward(b * 20)
        turtle.right(90)
        turtle.pendown()
        # Calculate the radius for the current arc
        radius = b * 20
        # Calculate the extent of the arc based on Fibonacci number
        extent = 90 if i % 4 < 2 else -90
        # Draw the arc
        draw_arc(turtle, radius / 2, extent)  # Halve the radius as it's the semi-circle radius
        # Prepare for the next square and arc
        a, b = b, a + b
        # Reposition the turtle to the bottom-right corner of the square
        turtle.penup()
        turtle.setpos(-20 * a, -20 * a)
        turtle.pendown()
        turtle.left(90)  # Reset turtle heading to the default


def draw_arc(turtle, radius, extent):
    """Draw an arc for the given radius and extent."""
    step_angle = 1
    step_length = 2 * math.pi * radius / 360  # Circumference formula
    for _ in range(extent):
        turtle.forward(step_length)
        turtle.left(step_angle if extent > 0 else -step_angle)


# Define a function to draw a golden spiral
golden_ratio = (1 + math.sqrt(5)) / 2  # Approximate golden ratio


def draw_golden_spiral(turtle, number_of_squares):
    """Draw a golden spiral starting with Fibonacci squares."""
    radius = 5  # Starting radius
    for i in range(number_of_squares):
        draw_arc(turtle, radius, 90)  # Draw a quarter circle arc
        radius *= golden_ratio  # Increase radius for the next arc


# Set up the screen and turtle
screen = t.Screen()
screen.setup(1000, 800)
fibonacci_turtle = t.Turtle()
fibonacci_turtle.pensize(3)
fibonacci_turtle.hideturtle()
fibonacci_turtle.speed(0)

# Draw Fibonacci squares and spiral
draw_fibonacci_squares(fibonacci_turtle, 5)  # Draw 8 Fibonacci squares
draw_golden_spiral(fibonacci_turtle, 10)  # Draw the golden spiral approximation

# Finish drawing and wait for user to click to close the window
screen.exitonclick()
