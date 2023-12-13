import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hien's Snake Game")
screen.tracer(0)

# Create instances of Snake, Food, and Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Keyboard bindings for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # Collision with food
    if snake.head.distance(food) < 15:  # distance method compare snake head to the food
        food.refresh()  # Move the food to a new random location
        scoreboard.increase_score()  # Increment the score
        snake.grow()  # Add a new segment to the snake

    # Collision with wall
    # Check if the snake's head has collided with the walls
    # The screen size is assumed to be 600x600, so the coordinates range from -300 to 300
    # Since the snake's head is not at the very edge due to its size, a margin is given (hence 280 instead of 300)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False  # Set the game's running state to False to stop the game loop
        scoreboard.game_over()  # Call the game_over method of the scoreboard to display the game over message

    # Collision with tail
    for segment in snake.segments[1:]:  # Skip the head with slice list
        if snake.head.distance(segment) < 10:
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display the game over message

screen.exitonclick()
