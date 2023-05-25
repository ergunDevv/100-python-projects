# import turtle

# # Class names generally created with pascal case.

# tim = turtle.Turtle()
# tim.shape("turtle")
# tim.tilt(45)
# tim.color("red", "green")
# tim.forward(100)
# # Defining object from classs
# my_screen = turtle.Screen()
# # Accessing the object's attribute
# print(my_screen.window_width)
# # Accessing the object's method
# my_screen.exitonclick()


# Pretty Table Package

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

print(table)
