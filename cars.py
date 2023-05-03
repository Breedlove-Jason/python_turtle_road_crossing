from turtle import Turtle
import random

COLOR_LIST = ["red", "orange", "yellow", "green", "blue", "purple"]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLOR_LIST))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.random_x = random.randint(-250, 250)
        self.random_y = random.randint(-250, 250)

    def move(self):
        self.forward(10)

    def gen_cars(self):
        for cars in range(9):
            cars = Cars()
            cars.move()
            if cars.distance(self.random_x, self.random_y) < 100:
                cars.goto(self.random_x, self.random_y)