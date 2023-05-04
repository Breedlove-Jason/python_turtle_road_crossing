from cars import Cars
import random


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_spacing = 100

    def generate_new_car(self):
        new_car = Cars()
        new_car.goto(random.randint(-250, 250), random.randint(-250, 250))
        for car in self.car_list:
            while new_car.distance(car) < self.car_spacing:
                new_car.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(-10)
