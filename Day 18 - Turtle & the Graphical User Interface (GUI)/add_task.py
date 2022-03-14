import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(1)

turtle.colormode(255)
colors = ['red', 'green', 'yellow', 'purple', 'blue', 'black', 'orange']
tim.speed(0)

directions = [0, 90, 180, 270]


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(int(360/6)):
    tim.circle(200)
    tim.right(6)
    tim.color(change_color())




screen = Screen()
screen.exitonclick()
