import turtle
import math
import random
def polygones(cote, x,y,rayon,color):
    
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    for i in range(0,cote+1):
        angle = i * (2 * math.pi / cote)
        turtle.goto(x+rayon * math.cos(angle)  , y+rayon * math.sin(angle))
    turtle.end_fill() 
    turtle.up()

turtle.up()
polygones(random.randint(3,10),random.randint(-500,500),random.randint(-500,500),random.randint(50,300),'black')
polygones(random.randint(3,10),random.randint(-500,500),random.randint(-500,500),random.randint(50,300),'blue')
polygones(random.randint(3,10),random.randint(-500,500),random.randint(-500,500),random.randint(50,300),'red')
polygones(random.randint(3,10),random.randint(-500,500),random.randint(-500,500),random.randint(50,300),'yellow')
turtle.done()
