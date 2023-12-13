from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")


class Scoreboard(Turtle):
    def __init__(self, score_limit):
        """Initialize the scoreboard."""
        super().__init__()
        self.score_limit = score_limit
        self.score = 0
        self.color("white")
        self.hideturtle()  # Hide the turtle object, only show the text
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.is_game_over = False

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 270)  # Left player's score
        self.write(f"Left Player's SCORE: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(250, 270)  # Right player's score
        self.write(f"Right Player's SCORE: {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        if self.l_score >= self.score_limit:
            self.game_over()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        if self.r_score >= self.score_limit:
            self.game_over()

    def game_over(self):
        """Display 'GAME OVER' message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        self.is_game_over = True  # Attribute to signal game over

