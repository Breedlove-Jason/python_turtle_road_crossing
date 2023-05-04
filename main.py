from turtle import Screen
from racer_turtle import RacerTurtle
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
# screen.tracer(0)
NUM_CARS = 11
racer_turtle = RacerTurtle(0, -280)

car_manager = CarManager()

for _ in range(NUM_CARS):
    car_manager.generate_new_car()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()

    # Check for collision with any car
    for car in car_manager.car_list:
        if car.distance(racer_turtle) < 20:
            racer_turtle.reset_position()
            break

    if racer_turtle.ycor() > 280:
        racer_turtle.reset_position()
        car_manager.generate_new_car()

    screen.listen()
    screen.onkey(racer_turtle.go_up, "Up")

screen.exitonclick()
