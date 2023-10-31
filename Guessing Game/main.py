# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

# Print the game logo.
print(logo)

# Constants for the number of turns based on difficulty.
EASY_LEVEL = 10
HARD_LEVEL = 5


# Function to set the game difficulty and return the number of turns allowed.
def set_difficulty():
    """Returns the number of turns based on chosen difficulty."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


# Function to check if the user's guess is correct and provide feedback.
def check_answer(guess, number):
    """Compares user_guess to random_number and returns boolean for correctness."""
    if guess > number:
        print("Too high.")
        return False
    elif guess < number:
        print("Too low.")
        return False
    else:
        print(f"You got it! 😄😄🎉🥳 The answer is {number}")
        return True


# Main game loop.
while True:
    # Generate a random number for the user to guess.
    random_number = random.randint(1, 100)
    # Get the user's chosen difficulty and number of turns.
    turns = set_difficulty()

    # Flag to determine if the game is over.
    game_over = False
    while not game_over:
        # User makes a guess.
        user_guess = int(input(f"Guess a number between 1 to 100: "))
        print(f"You have {turns} attempts remaining to guess the number.")

        # Check if the user's guess is correct.
        correct_guess = check_answer(user_guess, random_number)

        # End the game if the user guessed correctly or ran out of turns.
        if correct_guess or turns == 1:
            game_over = True
            if not correct_guess:
                print(f"You've run out of guesses, the correct number was {random_number}.")
        # Decrement the number of turns after each guess.
        turns -= 1

    # Ask the user if they want to play again.
    play_again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ").lower()
    if play_again != 'y':
        break



