import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "india-outline-map.gif"
screen.addshape(image)

turtle.shape(image)

"""get coordinates of each states"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("india.csv")
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states) <= 37:
    answer_state = screen.textinput(title=f"{len(guessed_stated)}/37 states correct",
                                    prompt="What's the another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for states in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("not_known.csv")
        break

    if answer_state in all_states:
        guessed_stated.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

