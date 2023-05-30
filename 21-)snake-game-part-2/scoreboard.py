from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 240)
        self.hideturtle()
        self.write(f"Score: {self.score}", align='center',
                   font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.undo()
        self.write(f"Score: {self.score}", align='center',
                   font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align='center',
                   font=("Courier", 24, "normal"))
