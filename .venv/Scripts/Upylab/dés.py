import random


def alea_dice(s):
    random.seed(s)
    a= 1
    b= 6
    x = random.randint(a,b)
    y = random.randint(a,b)
    z = random.randint(a,b)
    if((x==1 or y==1 or z == 1) and (x==2 or y==2 or z== 2) and (x==4 or y==4 or z == 4)):
        return True
    else:
        return False