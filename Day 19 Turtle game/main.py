from turtle import Turtle, Screen

# initialize the turtle
hien = Turtle()
screen = Screen()


# move forward function
def move_forward():
    hien.forward(10)


# Show the screen and set onkey to space bar to move forward function
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()