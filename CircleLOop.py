import turtle                # Import the Turtle library

bob = turtle.Turtle()        # Create an object
turtle.bgcolor('#0E1630')    # Change the background colour
bob.pensize(1)               # setting the pen thikness
bob.pencolor('#1FC4DA')      # Change pen colour to red


# Changing the speed of the turtle, 0 means the maximum speed
bob.speed(0)
bob.penup()                    # Stop drawing when moving

bob.goto((-50, 200))           # Move turtle to an absolute position.
bob.pendown()                  # Start drawing again when moving
bob.shape("turtle")            # Set the pen shape of the turtle

forwardistance = 0             # variable
Right = 0                      # variable
for i in range(220):
    bob.forward(forwardistance)
    bob.right(Right)
    forwardistance += 3
    Right += 1


turtle.done()                 # not to close the window at the end
