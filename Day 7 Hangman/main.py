import random
from Hangman_art import stages, logo
from Hangman_words import word_list

# sample word list
# word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display += "_"

lives = len(stages) - 1  # Setting lives based on the number of stages you have.

print(logo)  # Assuming you want to display the game logo at the start.

guessed_letters = []  # Step 1: Initialize an empty list for guessed letters.

# Main game loop
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # If the guessed letter is already in the display, inform the user.
    if guess in display:
        print(f"You've already guessed the letter {guess}")
    else:
        guessed_letters.append(guess)  # Step 2: Add the guessed letter to the list.

    # Check the chosen word's position and then if match, replace with the letter.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guessed letter is not in the chosen_word, reduce a life.
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word.")
        lives -= 1
        print(stages[lives])

    # Display the list of guessed letters to the user.
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    print(f"{' '.join(display)}")  # To display the current state of guessed word.

# End of the game
if lives == 0:
    print("You lose! The word was:", chosen_word)
else:
    print("Congratulations! You guessed the word:", chosen_word)
