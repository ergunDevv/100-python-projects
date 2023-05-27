from turtle import Turtle, Screen
import colorgram
import random
screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(-200, -200)
rgb_colors = []
colors = colorgram.extract('spot_paint.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

turtle.dot(20)


def draw_dots(height, width):
    for j in range(height):

        for i in range(width-1):
            color = (random.choice(rgb_colors))
            turtle.forward(50)
            turtle.dot(20, color)
        turtle.setheading(90)
        turtle.forward(50)
        if j % 2 == 0:
            turtle.setheading(180)
        else:
            turtle.setheading(0)


print(rgb_colors)
draw_dots(10, 10)

# turtle.shape("turtle")
# turtle.color("red", "green")
# turtle.dot()


# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# def change_color():
#     R = random.random()
#     B = random.random()
#     G = random.random()

#     turtle.pencolor(R, G, B)


# turtle.speed(100)


# def draw_circle(how_many_circle):
#     for i in range(0, how_many_circle):
#         change_color()
#         turtle.left(10)
#         turtle.circle(50)


# draw_circle(36)


# def flip_coin():
#     coin = random.randint(1, 3)
#     return coin == 1


# def random_walk(random_walk_num):
#     for i in range(random_walk_num):
#         change_color()
#         if flip_coin():
#             turtle.right(90)
#             turtle.forward(20)
#         else:
#             turtle.left(90)
#             turtle.forward(20)


# random_walk(500)
# def draw_shape(side):
#     change_color()
#     angle = 360/side
#     for i in range(side):
#         turtle.right(angle)
#         turtle.forward(100)


# draw_shape(3)

screen.exitonclick()
