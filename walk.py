from random import randint, shuffle
import turtle as t

def bounce_sam(move):
    """
    keeps the turtle object on the screen
    """
    # bounces sam back to the center of the screen so he cannot wander off the edges
    # you will need to check the coordinates of your screen using
    # print(t.screenwidth())
    # print(t.screenheight())
    # then do the math - my screen is 640 wide and 540 high...
    if (sam.xcor() - move >= -320 and sam.xcor() + move <= 320) and (sam.ycor() - move >= -270 and sam.ycor() + move <= 270):
        sam.fd(move)
    else:
        sam.penup()
        sam.goto(0,0)
        sam.pendown()

def get_colour():
    """
    returns a random rgb colour
    """
    red = randint(1, 255)
    green = randint(1, 255)
    blue = randint(1, 255)
    return (red, green, blue)

# main
sam = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")
t.colormode(255)
directions = [0, 90, 180, 270]
sam.pendown()
sam.pensize(5)
sam.speed(10)
move = 25

# move sam to make a colourful pattern
for i in range(500):
    colour = get_colour()
    sam.color(colour)
    bounce_sam(move)
    shuffle(directions)
    sam.setheading(directions[0])

screen.exitonclick()