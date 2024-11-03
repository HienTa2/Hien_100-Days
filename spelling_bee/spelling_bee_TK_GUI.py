import tkinter as tk
from tkinter import simpledialog, messagebox, Label, Entry, Button, Frame
import pyttsx3
import gtts
from playsound import playsound
from threading import Thread
import pandas as pd

# Load the words from the provided Excel file
file_path = r'C:\Users\Hien Ta\Downloads\speeling_bee_words.xlsx'
words_df = pd.read_excel(file_path, sheet_name='Sheet1')

# Fix column reference issue by using the actual column name
# Display available column names to verify correctness
available_columns = words_df.columns.tolist()
print(f"Available columns: {available_columns}")

# Assuming the actual column name is 'word'
words_list = words_df[words_df.columns[0]].dropna().tolist()  # Convert the first column to a list, excluding NaN values

# Split words into difficulty levels (simple logic based on word length)
easy_words = [word for word in words_list if len(word) <= 5]
medium_words = [word for word in words_list if 6 <= len(word) <= 8]
hard_words = [word for word in words_list if len(word) > 8]

# Main application class for the Spelling Bee game
class SpellingBeeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Spelling Bee Game")
        self.current_index = {'easy': 0, 'medium': 0, 'hard': 0}
        self.difficulty_var = tk.StringVar()

        # Frame for difficulty selection and buttons
        self.top_frame = Frame(master)
        self.top_frame.pack(pady=10)

        Label(self.top_frame, text="Select Difficulty:").grid(row=0, column=0, columnspan=3)

        # Difficulty Selection
        self.easy_button = tk.Radiobutton(self.top_frame, text="Easy", variable=self.difficulty_var, value="easy")
        self.medium_button = tk.Radiobutton(self.top_frame, text="Medium", variable=self.difficulty_var, value="medium")
        self.hard_button = tk.Radiobutton(self.top_frame, text="Hard", variable=self.difficulty_var, value="hard")

        self.easy_button.grid(row=1, column=0, padx=5)
        self.medium_button.grid(row=1, column=1, padx=5)
        self.hard_button.grid(row=1, column=2, padx=5)

        # Start Button
        self.start_button = tk.Button(self.top_frame, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Display score and quit button
        self.bottom_frame = Frame(master)
        self.bottom_frame.pack(pady=10)

        self.score_label = Label(self.bottom_frame, text="Score: 0")
        self.score_label.pack(side=tk.LEFT, padx=10)

        self.quit_button = Button(self.bottom_frame, text="Quit", command=master.quit)
        self.quit_button.pack(side=tk.RIGHT)

        # TTS Engine initialization
        # self.tts_engine = pyttsx3.init()
        self.current_word = None
        self.score = 0

    def get_word(self, difficulty_mode):
        word_list = {
            'easy': easy_words,
            'medium': medium_words,
            'hard': hard_words
        }.get(difficulty_mode, [])

        if word_list:
            word = word_list[self.current_index[difficulty_mode]]
            self.current_index[difficulty_mode] = (self.current_index[difficulty_mode] + 1) % len(word_list)
            return word
        return None

    def start_game(self):
        difficulty = self.difficulty_var.get()
        if not difficulty:
            messagebox.showinfo("Info", "Please select a difficulty level")
            return

        self.current_word = self.get_word(difficulty).strip()
        if self.current_word:
            self.say_word_gtts(self.current_word)
            self.ask_spelling()

    def ask_spelling(self):
        d = CustomDialog(self.master, "Spelling Bee Game", self.current_word, self.say_word_gtts)
        user_input = d.result

        if user_input is None:
            return

        if user_input.lower().strip() == self.current_word.lower():
            messagebox.showinfo("Result", "Correct!")
            self.score += 1
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct spelling is '{self.current_word}'")

        self.update_score()

        continue_game = messagebox.askyesno("Continue", f"Your score is {self.score}. Do you want to continue?")
        if continue_game:
            self.start_game()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def say_word_gtts(self, word):
        try:
            filename = f"{word}.mp3"
            tts = gtts.gTTS(word)
            tts.save(filename)
            playsound(filename)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred with the Google TTS: {e}")
        finally:
            import os
            if os.path.exists(filename):
                os.remove(filename)


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
        box = Frame(self)
        self.repeat_button = Button(box, text="Repeat Word", command=self.repeat_word)
        self.repeat_button.pack(side=tk.LEFT, padx=5, pady=5)
        ok_button = Button(box, text="Submit", command=self.ok)
        ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        cancel_button = Button(box, text="Cancel", command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", lambda event: self.ok())
        self.bind("<Escape>", lambda event: self.cancel())

        box.pack()

    def repeat_word(self):
        self.say_word_func(self.word)

    def apply(self):
        self.result = self.entry.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeApp(root)
    root.geometry("400x300")
    root.mainloop()