import turtle
from random import randint

turtle.Screen()
turtle.bgcolor("#0E1630")
turtle.speed(0)
turtle.hideturtle()

# moon
moon = turtle.Turtle()
moon.color("orange")
moon.shape("turtle")
moon.speed(0)
moon.hideturtle()
moon.up()
moon.goto(0, -200)
moon.color('orange')
moon.begin_fill()
moon.circle(200)
moon.end_fill()

turtle.up()
turtle.goto(50, -200)
turtle.color('#0E1630')
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

# stars
stars = turtle.Turtle()
stars.color("orange")
stars.shape("turtle")
stars.speed(0)


def star():
    turns = 8
    while turns > 0:
        stars.forward(25)
        stars.left(205)
        turns = turns-1


nums_stars = 0
while nums_stars < 90:
    x = randint(-400, 400)
    y = randint(-400, 400)
    star()
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    nums_stars = nums_stars + 1

turtle.done()
