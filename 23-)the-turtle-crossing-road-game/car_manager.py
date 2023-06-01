from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 1.3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(280, random.randint(-280, 280))
        self.cars_speed = 0

    def move(self, level):
        self.cars_speed = STARTING_MOVE_DISTANCE+MOVE_INCREMENT*level
        self.forward(self.cars_speed)
