import random
from turtle import Turtle, Screen

# Define the screen object globally so can be use outside of the function
screen = Screen()


# Wrap in a function, so we can use it to play again if user choose
def race_turtles():
    screen.setup(width=500, height=400)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    is_race_on = False
    all_turtles = []

    # Create 6 turtles, set their colors and initial positions
    for i in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[i])  # put turtle in starting position
        all_turtles.append(new_turtle)

    # Ask user to place a bet
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

    if user_bet:
        is_race_on = True

    # Main loop to run the race
    while is_race_on:
        score = 0
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    score += 1
                    print(f"You've won! The {winning_color} turtle is the winner! Score: {score}")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner! Score: {score}")
                is_race_on = False
                break

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    # Clear turtles from screen for next game
    for turtle in all_turtles:
        turtle.hideturtle()

    screen.clearscreen()


# Main game loop
play_again = True
while play_again:
    race_turtles()  # call function if want to play again
    play_again = screen.textinput("Play Again?", "Would you like to play again? (yes/no): ").lower() == "yes"
