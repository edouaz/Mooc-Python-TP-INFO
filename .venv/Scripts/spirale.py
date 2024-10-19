import turtle 
steps = 100
def spirale (color, thikness):
    turtle.color(color)
    turtle.width(thikness)
    for i in range(1,steps):
        turtle.circle((thikness/2)* i,90)

## stv tu peut mettre une boucle while pour que ca tourne a l'infinit


spirale('red',10)
turtle.done

