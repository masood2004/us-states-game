import turtle
import pandas as pd

# Set up screen
screen = turtle.Screen()
screen.title("U.S. State Game")

# Register the image as a background
screen.bgpic("blank_states_img.gif")  # Use this as a background image

# Create a new turtle for the game
game_turtle = turtle.Turtle()
game_turtle.hideturtle()  # Hide the turtle for the game interface

# Read state data
data = pd.read_csv("50_states.csv")

# Keep track of correct answers
guessed_states = []

# Loop for guessing states
while len(guessed_states) < 50:
    count = len(guessed_states)
    answer = screen.textinput(title=f"{count}/50 Correct States",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        # Create a new CSV file with the states that were missed
        missed_states = [
            state for state in data["state"].values if state not in guessed_states]
        missed_states_data = pd.DataFrame(missed_states, columns=["state"])
        missed_states_data.to_csv("missed_states.csv", index=False)
        break

    if answer in data["state"].values and answer not in guessed_states:
        guessed_states.append(answer)

        # Extract coordinates of the state
        state_data = data[data["state"] == answer]
        x = int(state_data["x"].values[0])
        y = int(state_data["y"].values[0])

        # Create a new turtle to write the state name at the correct location
        name_turtle = turtle.Turtle()
        name_turtle.hideturtle()  # Hide the turtle itself
        name_turtle.penup()
        name_turtle.goto(x, y)
        name_turtle.write(answer, align="center", font=("Arial", 12, "normal"))
        count += 1


turtle.mainloop()
