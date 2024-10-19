

def rendre_monnaie(prix,x20, x10, x5, x2,x1):
    ma_money = 0
    for a in range(x20):
        ma_money += 20
    for z in range(x10):
        ma_money += 10
    for e in range(x5):
        ma_money += 5
    for r in range(x2):
        ma_money += 2
    for t in range(x1):
        ma_money += 1
    if(ma_money == prix):
        return (0,0,0,0,0)
    elif(ma_money < prix):
        return (None,None,None,None,None)
    elif(ma_money > prix):
        to_return = ma_money - prix
        y20 = 0 
        y10 = 0
        y5 = 0 
        y2 = 0
        y1 = 0
        if to_return >= 20:
            while to_return >= 20:
                y20 +=1
                to_return -= 20
        if to_return >= 10:
            while to_return >= 10:
                y10 +=1
                to_return -= 10
        if to_return >= 5:
            while to_return >= 5:
                y5 +=1
                to_return -= 5
        if to_return >= 2:
            while to_return >= 2:
                y2 +=1
                to_return -= 2
        if to_return >= 1:
            while to_return >= 1:
                y1 +=1
                to_return -= 1
        return (y20,y10,y5,y2,y1)

            
