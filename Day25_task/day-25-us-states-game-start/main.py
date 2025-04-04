import turtle, pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

pen_game = turtle.Turtle()
pen_game.hideturtle()
pen_game.penup()
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
guessed_state = []
all_state_list = data.state.to_list()

while len(guessed_state) < len(data["state"]):
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 the State", prompt="What's another state's name?").title()
    state_column = data["state"]
    if answer_state == 'Exit':
        missing_state = [state for state in all_state_list if state not in guessed_state]
        # for state in all_state_list:
            # if state not in guessed_state:
            #     missing_state.append(state)
        print(missing_state)
        break
    for state in state_column:
        if answer_state == state and answer_state not in guessed_state:
            state_row = data[data.state == state]
            pen_game.goto(state_row['x'].item(), state_row['y'].item())
            pen_game.write(answer_state)
            guessed_state.append(answer_state)