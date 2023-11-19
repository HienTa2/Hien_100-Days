import random
from art import spelling_bee
import pyttsx3
from easy_words import easy_words
from medium_words import medium_words
from hard_words import hard_words

# Display the spelling bee logo
print(spelling_bee)


def get_word(difficulty_mode):
    # Function to get a random word based on the chosen difficulty level
    if difficulty_mode == "easy":
        return random.choice(easy_words)
    elif difficulty_mode == "medium":
        return random.choice(medium_words)
    elif difficulty_mode == "hard":
        return random.choice(hard_words)
    else:
        # Return None if an invalid difficulty level is chosen
        return None


def say_word(word):
    # Function to pronounce a word using text-to-speech
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def spelling_bee_game():
    # Main function to run the spelling bee game
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    score = 0

    try:
        while True:
            word = get_word(difficulty)
            if word:
                while True:  # Loop to allow for word repetition
                    print("Listen to the word:")
                    say_word(word)

                    # Ask if the user wants to hear the word again
                    repeat = input("Would you like to hear the word again? (yes/no): ").lower()
                    if repeat != "yes":
                        break

                # Prompt the user to spell the word
                user_input = input("Spell the word: ").lower()
                if user_input == word:
                    print("Correct!")
                    score += 1  # Increase score for correct spelling
                else:
                    print(f"Incorrect! The correct spelling is '{word}'")

                # Display the current score
                print(f"Current score: {score}")

                # Option for the user to continue or end the game
                continue_game = input("Continue? (yes/no): ").lower()
                if continue_game != "yes":
                    break
            else:
                # Inform the user of an invalid difficulty selection and break the loop
                print("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")
                break
    except KeyboardInterrupt:
        # Handle the keyboard interrupt and display the final score
        print(f"\nGame interrupted. Final score:", {score})


if __name__ == "__main__":
    spelling_bee_game()  # Start the game
