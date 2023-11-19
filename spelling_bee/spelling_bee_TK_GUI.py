import random
import tkinter as tk
from tkinter import simpledialog, messagebox, Label, Entry, Button
import pyttsx3
from easy_words import easy_words
from medium_words import medium_words
from hard_words import hard_words
from threading import Thread


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


class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title, word, say_word_func):
        self.word = word
        self.say_word_func = say_word_func
        super().__init__(parent, title)

    def body(self, master):
        Label(master, text="Spell the word:").grid(row=0)
        self.entry = Entry(master)
        self.entry.grid(row=0, column=1)
        return self.entry

    def buttonbox(self):
        box = tk.Frame(self)
        self.repeat_button = Button(box, text="Repeat Word", command=self.repeat_word)
        self.repeat_button.pack(side=tk.LEFT, padx=5, pady=5)
        Button(box, text="Submit", command=self.ok).pack(side=tk.LEFT, padx=5, pady=5)
        Button(box, text="Cancel", command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def repeat_word(self):
        self.say_word_func(self.word)

    def apply(self):
        self.result = self.entry.get()


def say_word(word, _=None):
    # Function to pronounce a word using text-to-speech in a separate thread
    def run():
        engine = pyttsx3.init()
        engine.say(word)
        engine.runAndWait()
    Thread(target=run).start()


class SpellingBeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Bee Game")

        # Difficulty selection
        self.difficulty_var = tk.StringVar()
        self.easy_button = tk.Radiobutton(root, text="Easy", variable=self.difficulty_var, value="easy")
        self.medium_button = tk.Radiobutton(root, text="Medium", variable=self.difficulty_var, value="medium")
        self.hard_button = tk.Radiobutton(root, text="Hard", variable=self.difficulty_var, value="hard")
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)

        self.easy_button.pack()
        self.medium_button.pack()
        self.hard_button.pack()
        self.start_button.pack()

        self.current_word = None
        self.score = 0

    def start_game(self):
        difficulty = self.difficulty_var.get()
        if not difficulty:
            messagebox.showinfo("Info", "Please select a difficulty level")
            return

        self.current_word = get_word(difficulty)
        if self.current_word:
            say_word(self.current_word)
            self.ask_spelling()

    def ask_spelling(self):
        d = CustomDialog(self.root, "Spelling Bee Game", self.current_word, say_word)
        user_input = d.result

        if user_input is None:
            return  # User cancelled

        if user_input.lower() == self.current_word:
            messagebox.showinfo("Result", "Correct!")
            self.score += 1
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct spelling is '{self.current_word}'")

        # Show score and ask if the user wants to continue
        continue_game = messagebox.askyesno("Continue", f"Your score is {self.score}. Do you want to continue?")
        if continue_game:
            self.start_game()


if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeApp(root)
    root.geometry("300x200")  # Adjust the size of the window
    root.mainloop()
