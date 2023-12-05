import turtle 
from turtle import colormode
import random
colormode(255)

pegasus = turtle.Turtle() # gets our turtle functions


turtle.bgcolor("black")
#               r  g  b using hexacode

pegasus.setpos(pegasus.xcor(), pegasus.ycor() + 100)
pegasus.speed(0)


pegasus.color(255, 20, 20) # outline goes first, fill color is next

def RandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r, g, b)
    return randomColor

def DrawSquareAndTurn(size, controlNumber, angle): 
    for i in range(4):
        pegasus.forward(size)
        pegasus.right(90)
    pegasus.right(angle) 

    controlNumber -= 1 
    if controlNumber != 0: 
        DrawSquareAndTurn(size, controlNumber, angle) 

def DrawTriangleAndTurn(size, controlNumber, angle): 
    for i in range(3):
        pegasus.forward(size)
        pegasus.right(120)

    pegasus.right(angle) 

    controlNumber -= 1 
    if controlNumber != 0: 
        DrawTriangleAndTurn(size, controlNumber, angle) 

def DrawStarAndTurn(size, controlNumber, angle): 
    for i in range(5):
        pegasus.forward(size)
        pegasus.circle(10)
        pegasus.left(216)

    pegasus.circle(10)
    pegasus.right(angle) 
    pegasus.forward(50)

    controlNumber -= 1 

    if controlNumber != 0: 
        pegasus.color(RandomColor())
        DrawStarAndTurn(size, controlNumber, angle) 

pegasus.begin_fill()

def clicked(*args):
    DrawStarAndTurn(200, 60, 21)

turtle.onscreenclick(clicked)


pegasus.end_fill()

turtle.done()