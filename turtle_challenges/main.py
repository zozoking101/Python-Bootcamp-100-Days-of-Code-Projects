from turtle import Turtle, Screen
# import heroes
import random
import colorgram

tim = Turtle()

tim.shape("turtle")
# tim.color("#aabbcc")
tim.pd()
tim.pensize(2)
string = "1234567890abcdef"
tim.speed("fastest")


def color_string():
    color = "#"
    for _ in range(6):
        v = random.choice(string)
        color += v
    return color


def polygon(n, length):
    for _ in range(n):
        tim.forward(length)
        tim.left(-360 / n)


def dashed_line(n, length):
    for _ in range(n):
        tim.forward(length)
        tim.pu()
        tim.forward(length)
        tim.pd()


def n_polygons():
    for _ in range(3, 11):
        polygon(_, 100)
        tim.color(color_string())


def left():
    tim.left(90)
    tim.forward(10)


def right():
    tim.left(90)
    tim.forward(10)


directions = [0, 90, 180, 270]

# for _ in range(500):
#     tim.forward(30)
#     tim.color(color_string())
#     tim.setheading(random.choice(directions))

polygon(4, 100)
dashed_line(10, 10)
n_polygons()
# print(heroes.gen())

# i = 0
# for _ in range(500):
#     tim.circle(100)
#     tim.color(color_string())
#     tim.setheading(i)
#     i += 5

screen = Screen()
screen.exitonclick()
