from cars import Cars
import random


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_spacing = 100
        self.car_speed = 10

    def generate_new_car(self, x=None, y=None):
        new_car = Cars()
        if x is None or y is None:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
        new_car.goto(x, y)
        for car in self.car_list:
            while new_car.distance(car) < self.car_spacing:
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                new_car.goto(x, y)
        self.car_list.append(new_car)

    def check_car_position(self, car):
        if car.xcor() < -350:
            self.car_list.remove(car)
            self.generate_new_car(x=300, y=random.randint(-250, 250))

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)
            self.check_car_position(car)
