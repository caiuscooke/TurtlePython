import turtle 
tom = turtle.Turtle()

tom.speed(5)
tom.color('Red')
tom.fillcolor('Blue')
tom.pensize(1)
tom.shape('turtle')

def square():
    for i in range(0, 4):
        tom.forward(100)
        tom.right(90)


tom.begin_fill()

square()
tom.penup()
tom.forward(150)
tom.pendown()
square()

tom.end_fill()

turtle.done()