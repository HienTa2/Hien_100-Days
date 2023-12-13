from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()  # Call the initializer of the parent class (Turtle)
        self.shape("square")  # Set the shape of the paddle
        self.color("white")  # Set the color of the paddle
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle to the desired size
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(position)  # Move the paddle to the specified position

    def move_up(self):
        if self.ycor() < 250:  # Boundary check for upper limit
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -250:  # Boundary check for lower limit
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
