import turtle


t = turtle.Turtle()
t.speed(0)
t.up()
t.goto((0, -200))
t.pendown()
turtle.bgcolor('#0E1630')


for i in range(100):
    for colors in ["purple", "blue", "cyan", "green", "yellow", "orange", "red"]:
        t.color(colors)
        t.circle(i)
        t.forward(20)
        t.left(4)


turtle.done()
