from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def move_left():
    turtle.left(10)


def move_right():
    turtle.right(10)


def reset():
    turtle.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=reset)
screen.exitonclick()
