import random
from art import logo, vs
from game_data import data
from replit import clear

# Display the game logo.
print(logo)


def format_data(account):
    """
    Takes an account dictionary as input and returns a formatted string
    representing the account's name, description, and country.
    """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answers(guess, a_followers, b_followers):
    """
    Compares follower counts of two accounts and checks the user's guess.
    Returns True if the user's guess matches the account with more followers,
    False otherwise.
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Initialize user's score to 0 at the start.
score = 0

# Main game loop.
while True:
    # Randomly select two different accounts from the data.
    account_a = random.choice(data)
    account_b = random.choice(data)

    # Ensure both accounts are different.
    while account_a == account_b:
        account_b = random.choice(data)

    # Display formatted data for both accounts.
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Prompt the user to guess which account has more followers.
    user_guess = input("Who has more followers? Type 'A' or 'B' ").lower()

    # Retrieve follower counts for both accounts.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Determine if the user's guess is correct.
    is_correct = check_answers(user_guess, a_follower_count, b_follower_count)

    # clear the screen for the next question.
    clear()
    print(logo)

    # Update score and provide feedback based on the correctness of the guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        break

    # Ask the user if they wish to continue playing.
    continue_game = input("Do you want to play again? Type 'y' for yes, 'n' for no: ").lower()
    if continue_game == 'n':
        break
