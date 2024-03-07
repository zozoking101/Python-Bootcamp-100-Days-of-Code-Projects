import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
    

# turtle.onscreenclick(get_mouse_click_coor)

guessed_states = []

while len(guessed_states) < 50: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()
    states = data["state"].to_list()
    x_values = data.x.to_list()
    y_values = data.y.to_list()

    if answer_state == "Exit":
        # states to learn
        missing = []
        for state in states:
            if state not in guessed_states:
                missing.append(state)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in states:
        guessed_states.append(answer_state)
        i = states.index(answer_state.title())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        (x, y) = (x_values[i], y_values[i])
        t.goto((x, y))
        t.write(answer_state)
                