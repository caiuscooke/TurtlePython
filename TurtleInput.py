import turtle

bob = turtle.Turtle()
bob.speed(-1)
bob.pensize(10)
bob.shape('turtle')

colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple' ]

x = 0

def nextColor():
    global color
    global x
    if x < len(colorList) - 1:
        x += 1
        color = colorList[x]
        
    bob.color(color)

def prevColor():
    global color
    global x
    if x > 0:
        x -= 1
        color = colorList[x]

    bob.color(color)
    
def up():
    bob.setheading(90)
    bob.forward(10)

def down():
    bob.setheading(270)
    bob.forward(10)

def left():
    bob.setheading(180)
    bob.forward(10)

def right():
    bob.setheading(0)
    bob.forward(10)

def rightArrow():
    nextColor()
    print(x)
    print(color)
    

def leftArrow():
    prevColor()
    print(x)
    print(color)
    

def spaceUp():
    bob.penup()
def spaceDown():
    bob.pendown()

def clear():
    bob.clear()

turtle.listen()

turtle.onkeypress(up, 'w')
turtle.onkeypress(down, 's')
turtle.onkeypress(left, 'a')
turtle.onkeypress(right, 'd')
turtle.onkey(rightArrow, 'Right')
turtle.onkey(leftArrow, 'Left')
turtle.onkeypress(spaceUp, 'space')
turtle.onkeyrelease(spaceDown, 'space')
turtle.onkey(clear, 'Delete')

turtle.mainloop()
