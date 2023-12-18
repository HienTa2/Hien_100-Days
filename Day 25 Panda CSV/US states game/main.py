import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
# add the image as a shape in turtle
screen.addshape(image)
# show the image/gif
turtle.shape(image)


# Load the data
data = pandas.read_csv("50_states.csv")
# Convert all state names to title case for comparison
data["state"] = data["state"].str.lower()
guess_states = []


while len(guess_states) < 50:
    # Get user input
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct",
                                    prompt="What's the name of the state?").lower()

    # Exit the game if the user types 'Exit'
    if answer_state == "exit":
        # get the states that were missed and add it as a csv file
        missing_states = [state for state in data["state"] if state not in guess_states]  # list comprehension
        df = pandas.DataFrame(missing_states, columns=["states"])
        df.to_csv("missed_states.csv")
        break

    # check is answer_state is in the "state" column in csv file
    if answer_state in data["state"].values and answer_state not in guess_states:
        guess_states.append(answer_state)  # Add the correctly guessed
        # Get the row of the state
        state_data = data[data["state"] == answer_state]
        x = state_data['x'].values[0]
        y = state_data['y'].values[0]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer_state.title(), align="center", font=("Arial", 8, "normal"))
    else:
        print("That's not a state in the dataset.")


# function to get the x, y coor from mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()
