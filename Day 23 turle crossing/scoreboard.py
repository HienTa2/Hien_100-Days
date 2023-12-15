from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()  # Hide the turtle object, only show the text
        self.penup()
        self.goto(-220, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display 'GAME OVER' message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))




