from turtle import Turtle

# Constants defining the starting position and movement of the snake
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The first segment is the head of the snake

    def create_snake(self):
        """Create the initial snake with predefined segments."""
        for position in STARTING_POSITION:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def add_segment(self, position):
        """Adds a new segment at the specified position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self):
        """Add a new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        """Move the snake forward by moving each segment to the position of the previous one."""
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Methods to change the direction of the snake's head
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
