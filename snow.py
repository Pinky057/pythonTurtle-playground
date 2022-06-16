import turtle                       # Import the Turtle library

snowTurtle = turtle.Turtle()         # Create an object
turtle.bgcolor('#364C96')           # Change background colour
snowTurtle.pensize(4)
colors = ["#EAEBED", "#99D2FF", "#94AC64"]


snowTurtle.penup()                # Stop drawing when moving
snowTurtle.goto((-200, 0))        # Move turtle to an absolute position.

snowTurtle.pendown()              # Start drawing when moving
snowTurtle.shape("turtle")
# Changing the speed of the turtle, 0 means the maximum speed
snowTurtle.speed(0)


def snow(length, n):
    if n == 0:
        snowTurtle.forward(length)

    else:
        length /= 3
        n -= 1
        snow(length, n)
        snowTurtle.right(65)
        snow(length, n)
        snowTurtle.left(130)
        snow(length, n)
        snowTurtle.right(65)
        snow(length, n)


for side in range(3):

    # Choose a colour of the side from the array
    snowTurtle.color(colors[side])
    snow(500, 4)
    snowTurtle.left(120)


turtle.done()  # To not close the window at the end
