from turtle import *

speed(0)
bgcolor("#364C96")


# moon drawing
up()
goto(-20, -100)
color('orange')
begin_fill()
circle(200)
end_fill()

up()
goto(30, -100)
color('#364C96')
begin_fill()
circle(200)
end_fill()


# Grass
penup()
goto(-450, -150)
pendown()
color("#5D781B")
begin_fill()
for i in range(6):
    forward(900)
    right(90)
    forward(400)
    right(90)
end_fill()

# Left Mountain
penup()
goto(-400, -150)
pendown()
color("#FF9677")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# Right Mountain
penup()
goto(100, -150)
pendown()
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# Middle Mountain
penup()
goto(-160, -150)
pendown()
color("#974063")
begin_fill()
for i in range(3):
    forward(400)
    left(120)
end_fill()

# Middle Mountain Ice Cap
penup()
goto(-35, 70)
pendown()
color("white")
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
forward(45)
right(85)
forward(65)
left(160)
forward(150)
end_fill()

# Left Mountain Ice Cap
penup()
goto(-215, 55)
pendown()
color("snow")
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()

# Right Mountain Ice Cap
penup()
goto(203, 40)
pendown()
begin_fill()
forward(95)
right(120)
forward(80)
right(150)
forward(50)
left(70)
end_fill()

left(50)


# Tree

def tree():
    # Tree trunk
    color("saddlebrown")
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()

    # Turn the turtle around
    forward(10)
    left(90)
    forward(5)

    # Leaves on tree
    color("#295D09")
    begin_fill()
    circle(25)
    end_fill()

    right(90)


# Plant the first tree
penup()
goto(-25, -200)
pendown()
tree()

# Plant the second tree
penup()
goto(200, -150)
pendown()
tree()

# Plant the third tree
penup()
goto(300, -250)
pendown()
tree()

# Plant the fourth tree
penup()
goto(-300, -250)
pendown()
tree()

# Plant the fifth tree
penup()
goto(-200, -150)
pendown()
tree()
hideturtle()
done()
