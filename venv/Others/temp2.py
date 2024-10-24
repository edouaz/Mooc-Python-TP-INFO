import math

b = str(input())
a = float(input())
if b == "T" or b =="C" or b=="O" or b=="D" or b=="I" : 
    if b=="T":
        print(((math.sqrt(2)/12) * (a**3)))
    elif b=="C":
        print(a**3)
    elif b=="O":
        print((math.sqrt(2)/3)*(a**3))
    elif b=="D":
        print(((15+(7*math.sqrt(5)))/4)* (a**3))
    elif b=="I":
        print((5*(3+math.sqrt(5))/12)* (a**3))
else:
    print("Polyèdre non connu")


