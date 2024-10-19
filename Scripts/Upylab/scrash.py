import math
import turtle

# Rayon de l'hexagone
r = int(input("Rayon :"))
p = int(input("Points :"))
turtle.begin_fill()

# Commencer le remplissage
for i in range(p):
    _angle = i * (2* math.pi/p)
    x = r * math.cos(_angle)
    y = r * math.sin(_angle)
    turtle.goto(x,y)

_angle = 1 * (2* math.pi/1)
x = r * math.cos(_angle)
y = r * math.sin(_angle)
turtle.goto(x,y)
# Fermer le polygone et finir le remplissage
turtle.end_fill()

# Cacher la tortue
turtle.hideturtle()

# Finaliser le dessin
turtle.done()
