import turtle
from turtle import Turtle, Screen  # Turtle CLASS
from unittest.mock import right
# import heroes
# print(heroes.gen())
import random

color_list = ["maroon2" , "gold" , "teal", "chocolate3" ]
shape_list = ["square" , "circle" , "triangle"]

timmy = Turtle()
timmy.color(random.choice(color_list))
timmy.penup()   # lift pen up while muving

# # draw square
# timmy_the_turtle.shape("square")    # it draw a small square
# # using for loop with range
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

for x in range(10):
    for y in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(5)
        timmy.forward(30)

    timmy.backward(30 * 10)
    timmy.right(90)
    timmy.forward(30)
    timmy.left(90)

# this goes to the end
screen = Screen()
screen.exitonclick()