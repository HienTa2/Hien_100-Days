from turtle import *

# Hien = Turtle()
# print(Hien)
# Hien.shape("turtle")
# Hien.color("coral")
# Hien.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
#
# # continue running until user click.
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)