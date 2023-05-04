from turtle import Screen
from racer_turtle import RacerTurtle
from car_manager import CarManager
from scoreboard import Scoreboard
import time

NUM_CARS = 5
CAR_SPEED = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

racer_turtle = RacerTurtle(0, -280)
car_manager = CarManager()
score = Scoreboard()

for _ in range(NUM_CARS):
    car_manager.generate_new_car()


game_is_on = True
while game_is_on:
    car_manager.car_speed = CAR_SPEED
    screen.update()
    time.sleep(0.2)

    car_manager.move_cars()

    # Check for collision with any car
    for car in car_manager.car_list:
        if car.distance(racer_turtle) < 20:
            score.game_over()
            racer_turtle.reset_position()
            break

    if racer_turtle.ycor() > 280:
        racer_turtle.reset_position()
        car_manager.generate_new_car()
        score.increase_score()
        score.update_scoreboard()
        CAR_SPEED += 5

    screen.listen()
    screen.onkey(racer_turtle.go_up, "Up")
    screen.onkey(racer_turtle.stop_turtle(), "Space")

screen.exitonclick()
