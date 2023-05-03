from turtle import Screen
from racer_turtle import RacerTurtle
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
# screen.tracer(0)

racer_turtle = RacerTurtle(0, -280)

car = Cars()
car.gen_cars()
# for cars in range(9):
#     car = Cars()

game_is_on = True
while game_is_on:
    screen.update()
    # car.move()
    if car.distance(racer_turtle) < 20:
        racer_turtle.reset_position()
    if racer_turtle.ycor() > 280:
        racer_turtle.reset_position()
    screen.listen()
    screen.onkey(racer_turtle.go_up, "Up")


screen.exitonclick()
