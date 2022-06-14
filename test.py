import turtle
turtle.getscreen().bgcolor("#0E1630")

turtle.penup()
turtle.goto((-200, 100))
turtle.pendown()
turtle.begin_fill()

for i in range(50):
    for colors in ["#87E1C7", "blue", "red", "cyan", "gray", "green", "#94AC64", "#E65C4F"]:
        turtle.color(colors)
        turtle.forward(60)
    turtle.left(170)

turtle.end_fill()
turtle.done()
