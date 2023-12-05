import turtle
import random

bob = turtle.Turtle()

colorList = ['red', 'yellow', 'black', 'green', 'blue', 'purple', 'orange', 'chocolate', 'aquamarine', 'deeppink', 'azure', 'maroon', 'magenta', 'royalblue3', 'salmon', 'wheat', 'peru', 'gold2', 'khaki']

def randomCircles(turtle1, repeat):
    turtle1.shape('turtle')
    turtle1.speed(-1)

    for i in range(repeat):
        
        turtle1.pensize(random.randint(1, 15))

        randomRadius = random.randint(0, 100)
        randomX = random.randint(-300, 300)
        randomY = random.randint(-300, 300)
 
        randomColor1 = random.choice(colorList)
        randomColor2 = random.choice(colorList)

        turtle1.penup()
        
        turtle1.setpos(randomX, randomY)
        
        turtle1.pendown()
        
        turtle1.begin_fill()
        
        turtle1.color(randomColor1, randomColor2)
        
        turtle1.circle(randomRadius)
        
        turtle1.end_fill()
        
randomCircles(bob, 200)

turtle.done()