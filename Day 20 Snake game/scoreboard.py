from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()  # Hide the turtle object, only show the text
        self.penup()
        self.goto(0, 270)  # Position at the top of the screen
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display 'GAME OVER' message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
