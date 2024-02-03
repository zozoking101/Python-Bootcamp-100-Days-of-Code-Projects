import turtle
import random

color_list = [(28, 111, 169), (139, 164, 186), (201, 140, 166), (214, 158, 95), (188, 175, 19),
              (235, 212, 75), (66, 24, 32), (20, 137, 66), (146, 17, 35), (126, 73, 94), (184, 69, 38),
              (228, 168, 196), (30, 178, 96), (7, 105, 62), (48, 29, 27), (236, 77, 36), (241, 218, 4),
              (110, 190, 138), (32, 33, 41), (27, 170, 188), (181, 95, 115), (188, 183, 212), (142, 23, 18),
              (156, 208, 216), (152, 214, 177), (242, 166, 154)]

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.pu()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(320)
timmy.setheading(0)

for _ in range(10):
    for __ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.backward(500)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)

turtle.Screen()
turtle.exitonclick()
