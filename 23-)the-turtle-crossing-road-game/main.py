import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

cars = []
level = 1
car = CarManager()
scoreboard = Scoreboard()
cars.append(car)
screen.onkey(player.move, 'Up')
car_number = 0
max_car_number = 10
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
        car.move(level)

    while car_number < max_car_number:
        car = CarManager()
        cars.append(car)
        car_number += 1

    if random.random() > 0.8:
        max_car_number += 1

    if player.ycor() > 280:
        # car.level_up()
        level += 1
        scoreboard.level_up()
        player.reset_position()
