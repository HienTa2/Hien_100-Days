# Importing necessary classes and data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initializing an empty list to store the questions for the quiz
question_bank = []
for question in question_data:
    # Extracting question text and answer from each question in the data
    question_text = question["text"]
    question_answer = question["answer"]
    # Creating a Question object with the extracted data
    new_question = Question(question_text, question_answer)
    # Adding the newly created question to the question bank
    question_bank.append(new_question)

# Creating an instance of QuizBrain, passing in the question bank
quiz = QuizBrain(question_bank)

# Running the quiz in a loop until all questions have been asked
while quiz.still_has_question():
    # Displaying the next question and checking for the continuation of the quiz
    # If the user answers incorrectly, the quiz will end
    if not quiz.next_question():
        break

print(f"Your final score is {quiz.score}/{quiz.question_number}.")