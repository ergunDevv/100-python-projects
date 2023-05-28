from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(
    title="Make your guess ", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = {}
i = 0
for color in colors:
    name = f"turtle_{color}"
    turtles[name] = turtles.get(name, Turtle(shape="turtle"))
    turtles[name].penup()
    turtles[name].color(f"{color}")
    turtles[name].goto(-230, -90+i)
    i += 30

if user_guess:
    is_race_on = True
winner = ""
while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtles[turtle].forward(random_distance)
        if turtles[turtle].xcor() >= 230:
            winner = turtle
            is_race_on = False
if user_guess == winner:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()
