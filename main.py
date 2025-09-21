import turtle
import pandas

screen = turtle.Screen()
image = "indian_states_blank.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
all_state = data.state.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 30 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States guessed",prompt="Write a name of state.").title()
    if answer_state=="Exit" :
        for state in all_state:
            if state not in guessed_states:
             missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x_state=int(state_data.x.item())
        y_state=int(state_data.y.item())
        t.goto(x_state,y_state)
        t.write(arg=answer_state,align="center")
screen.exitonclick()
