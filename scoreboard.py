from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("black")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} ", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\nHigh Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
