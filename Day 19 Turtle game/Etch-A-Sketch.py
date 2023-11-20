from turtle import Turtle, Screen

# Initialize the turtle and screen
hien = Turtle()
screen = Screen()


# Function to move the turtle forward
def move_forward():
    hien.forward(10)  # Move the turtle forward by 10 units


# Function to move the turtle backward
def move_backward():
    hien.backward(10)  # Move the turtle backward by 10 units


# Function to turn the turtle left
def turn_left():
    hien.left(10)  # Turn the turtle left by 10 degrees


# Function to turn the turtle right
def turn_right():
    hien.right(10)  # Turn the turtle right by 10 degrees


# Function to clear the drawing and reset the turtle's position
def clear():
    hien.clear()  # Clear the turtle's drawings from the screen
    hien.penup()  # Lift the pen up so it doesn't draw while moving to home position
    hien.home()  # Move the turtle to its original position
    hien.pendown()  # Put the pen down to start drawing again


# Set up the screen to listen for key presses
screen.listen()
screen.onkey(move_forward, "w")  # Press 'w' to move forward
screen.onkey(move_backward, "s")  # Press 's' to move backward
screen.onkey(turn_left, "a")  # Press 'a' to turn left
screen.onkey(turn_right, "d")  # Press 'd' to turn right
screen.onkey(clear, "c")  # Press 'c' to clear drawing and reset position

# Click on the screen to exit the program
screen.exitonclick()
