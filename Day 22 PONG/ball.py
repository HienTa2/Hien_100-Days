import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self, ball_speed_increment):
        """Initialize the ball object."""
        super().__init__()
        self.ball_speed_increment = ball_speed_increment
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.50, stretch_wid=.50)  # Small circle shape
        self.color("white")
        self.speed(0)  # Drawing speed
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        print(new_x, new_y)  # see where the ball cross the line

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.x_move *= self.ball_speed_increment
        self.y_move *= self.ball_speed_increment

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.increase_speed()
