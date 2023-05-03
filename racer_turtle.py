from turtle import Turtle


class RacerTurtle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(x, y)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def go_up(self):
        self.setheading(90)
        self.forward(10)

    def reset_position(self):
        self.goto(0, -280)
