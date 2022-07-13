import turtle

t = turtle.Turtle()

t.speed(30)
turtle.bgcolor('#0E1630')

for i in range(300):
    t.color("orange")
    t.circle(i)
    t.forward(2)
    t.left(6)

turtle.done()
