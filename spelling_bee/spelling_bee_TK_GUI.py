import tkinter as tk
from tkinter import simpledialog, messagebox, Label, Entry, Button
import pyttsx3
from threading import Thread
from easy_words import easy_words  # Importing word lists for different difficulty levels
from medium_words import medium_words
from hard_words import hard_words


# Main application class for the Spelling Bee game
class SpellingBeeApp:
    # Initialize the main application
    def __init__(self, master):
        self.master = master  # Main window of the application
        self.master.title("Spelling Bee Game")  # Set the window title
        # Indexes to track current word for each difficulty
        self.current_index = {'easy': 0, 'medium': 0, 'hard': 0}
        self.difficulty_var = tk.StringVar()  # Variable to store selected difficulty level
        # Radio buttons for difficulty selection
        self.easy_button = tk.Radiobutton(master, text="Easy", variable=self.difficulty_var, value="easy")
        self.medium_button = tk.Radiobutton(master, text="Medium", variable=self.difficulty_var, value="medium")
        self.hard_button = tk.Radiobutton(master, text="Hard", variable=self.difficulty_var, value="hard")
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)  # Start button

        # Pack the radio buttons and start button into the window
        self.easy_button.pack()
        self.medium_button.pack()
        self.hard_button.pack()
        self.start_button.pack()

        self.current_word = None  # The current word to be spelled
        self.score = 0  # The player's score

    # Function to retrieve the next word from the selected difficulty list
    def get_word(self, difficulty_mode):
        word_list = {
            'easy': easy_words,
            'medium': medium_words,
            'hard': hard_words
        }.get(difficulty_mode, [])  # Get the appropriate list based on difficulty

        # Retrieve and return the next word in the list
        if word_list:
            word = word_list[self.current_index[difficulty_mode]]
            self.current_index[difficulty_mode] = (self.current_index[difficulty_mode] + 1) % len(word_list)
            return word
        return None

    # Function to start the game and handle word retrieval and scoring
    def start_game(self):
        difficulty = self.difficulty_var.get()
        if not difficulty:
            messagebox.showinfo("Info", "Please select a difficulty level")
            return

        self.current_word = self.get_word(difficulty)
        if self.current_word:
            say_word(self.current_word)  # Speak out the current word
            self.ask_spelling()  # Prompt user to spell the word

    # Function to display the custom dialog for user input and check spelling
    def ask_spelling(self):
        d = CustomDialog(self.master, "Spelling Bee Game", self.current_word, say_word)
        user_input = d.result

        if user_input is None:
            return  # Exit if user cancelled

        # Check if user spelled the word correctly and update score
        if user_input.lower() == self.current_word:
            messagebox.showinfo("Result", "Correct!")
            self.score += 1
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct spelling is '{self.current_word}'")

        # Ask user if they want to continue and start a new game if so
        continue_game = messagebox.askyesno("Continue", f"Your score is {self.score}. Do you want to continue?")
        if continue_game:
            self.start_game()


# Custom dialog class for the spelling input
class CustomDialog(simpledialog.Dialog):
    # Initialize the custom dialog
    def __init__(self, parent, title, word, say_word_func):
        self.word = word  # The word to be spelled
        self.say_word_func = say_word_func  # Function to pronounce the word
        super().__init__(parent, title)

    # Create the dialog body with an entry widget for spelling input
    def body(self, master):
        Label(master, text="Spell the word:").grid(row=0)
        self.entry = Entry(master)
        self.entry.grid(row=0, column=1)
        return self.entry

    # Add buttons for repeating the word, submitting the answer, and cancelling
    def buttonbox(self):
        box = tk.Frame(self)
        self.repeat_button = Button(box, text="Repeat Word", command=self.repeat_word)
        self.repeat_button.pack(side=tk.LEFT, padx=5, pady=5)
        ok_button = Button(box, text="Submit", command=self.ok)
        ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        cancel_button = Button(box, text="Cancel", command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", lambda event: self.ok())
        self.bind("<Escape>", lambda event: self.cancel())

        box.pack()

    # Function to call the word pronunciation function
    def repeat_word(self):
        self.say_word_func(self.word)

    # Apply the user's spelling input
    def apply(self):
        self.result = self.entry.get()


# Function to use text-to-speech to pronounce the word
# Function to pronounce a word using text-to-speech in a separate thread
def say_word(word):
    """Pronounce the given word using text-to-speech."""

    def run():
        engine = pyttsx3.init()
        engine.say(word)
        engine.runAndWait()

    # Start the pronunciation in a separate thread to prevent blocking the UI
    Thread(target=run).start()


# Main script execution: initialize the app and start the main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeApp(root)
    root.geometry("300x200")
    root.mainloop()
