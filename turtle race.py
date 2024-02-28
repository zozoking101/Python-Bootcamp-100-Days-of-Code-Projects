from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=650,height=650)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_values = [70, 35, 0, -35, -70, -105]
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-270,y=y_values[i])
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            w_color = turtle.pencolor()
            if w_color == user_bet:
                print(f"You've won! The {w_color} turtle won the race!")
            else:
                print(f"You Lost! The {w_color} turtle won the race!")
        d = random.randint(0,10)
        turtle.forward(d)
        
screen.exitonclick()