import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"25-)pandas-and-csv-data\u.s-states-quiz\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv(
    r"25-)pandas-and-csv-data\u.s-states-quiz\50_states.csv")

# print(data)


def create_text(state, x, y):
    turtle_text = turtle.Turtle()
    turtle_text.penup()
    turtle_text.hideturtle()
    turtle_text.setposition(int(x), int(y))
    turtle_text.write(state)


guessed_states = []
missing_states = []
is_game_on = True
score = 0
while is_game_on:
    answer_state = screen.textinput(
        title=f"{score}/50 States Correct", prompt="What's another state's name?")
    for state in data['state']:
        if answer_state.lower() == state.lower():
            guessed_states.append(state)
            score += 1
            x = data[data.state == state].x
            y = data[data.state == state].y
            create_text(state, x, y)
    if score >= 50:
        is_game_on = False
    if answer_state == "exit":
        for state in data['state']:
            if state not in guessed_states:
                missing_states.append(state)

        states_final = pandas.DataFrame(missing_states)
        states_final.to_csv(
            r"25-)pandas-and-csv-data\u.s-states-quiz\states_final.csv")
        is_game_on = False

# turtle.mainloop()
