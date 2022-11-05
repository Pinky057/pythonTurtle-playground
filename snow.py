import turtle                            # Import the Turtle library


snowTurtle = turtle.Turtle()             # create an object
turtle.bgcolor('#364c96')                # change the background color
snowTurtle.pensize(4)                    # setting the pensize property
colors = ["#EAEBED", "#99D2FF", "#94AC64"]


snowTurtle.penup()           # stop drawing when moving
snowTurtle.goto((-200, 0))  # move turtle to an absolute position

snowTurtle.pendown()           # start drawing when moving
snowTurtle.shape("turtle")     # shpe the pen to turtle shape
snowTurtle.speed(0)            # sets the speed, 0 is the maximum speed


def snow(length, n):
    if n == 0:
        snowTurtle.forward(length)

    else:
        length /= 3                   # abriviation of this is x= x/ y
        n -= 1                        # abriviation of this is x =x-y
        snow(length, n)
        snowTurtle.right(65)
        snow(length, n)
        snowTurtle.left(130)
        snow(length, n)
        snowTurtle.right(65)
        snow(length, n)


for side in range(3):
    snowTurtle.color(colors[side])
    snow(500, 4)
    snowTurtle.left(120)

turtle.done()   # to not colse the window at the end
