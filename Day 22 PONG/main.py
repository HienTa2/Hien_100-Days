import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Game constants
PADDLE_MOVE_DISTANCE = 30
BALL_SPEED_INCREMENT = 1.1
SCORE_LIMIT = 5

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Hien's Pong game")
screen.tracer(0)  # remove the animation of the paddle when game start

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball(BALL_SPEED_INCREMENT)
scoreboard = Scoreboard(SCORE_LIMIT)

# controls of the paddles
screen.listen()
screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "8")
screen.onkey(r_paddle.move_down, "2")

game_is_on = True
while game_is_on:
    time.sleep(.06)
    screen.update()  # manual update to work with the tracer function
    ball.move_ball()

    # detect the ball with wall for top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # detect if right paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        # Add score for left player or any other logic
        scoreboard.l_point()

    # detect if left paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        # Add score for right player or any other logic
        scoreboard.r_point()

    # Check if the game is over
    if scoreboard.is_game_over:
        break  # Exit the game loop

screen.exitonclick()
