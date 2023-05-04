from turtle import Turtle
import random


class Cars(Turtle):
    COLOR_LIST = ["red", "orange", "yellow", "green", "blue", "purple"]

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(self.COLOR_LIST))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(180)
