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
        self.car_list = []

    def move(self):
        for car in self.car_list:
            car.forward(-10)

    def gen_cars(self):
        for cars in range(9):
            cars = Cars()
            self.car_list.append(cars)
            # cars.move()
            if cars.distance(self.random_x, self.random_y) < 100:
                self.car_list.remove(cars)
                cars = Cars()
                self.car_list.append(cars)
                cars.goto(self.random_x, self.random_y)

                # if self.random_x > 250:
                #     cars = Cars()
                #     self.car_list.append(cars)
                #     cars.goto(-250, self.random_y)
