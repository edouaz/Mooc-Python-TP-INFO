
def duree (debut : tuple , fin : tuple) -> tuple:
    hour_1 = debut[0]
    hour_2 = fin[0]
    minuts_1 = debut[1]
    minuts_2 = fin[1]
    hour_Past = 0
    minuts_Past = 0
    isSameDay = sameDay(hour_1, hour_2)
    if isSameDay :
        hour_Past = hour_2 - hour_1
        minuts_Past = minutePast(minuts_1, minuts_2)
        if subHour(minuts_1,minuts_2):
            hour_Past -= 1
        return (hour_Past,minuts_Past)
    else:
        hour_Past = (24 - hour_1) + hour_2
        minuts_Past = minutePast(minuts_1, minuts_2)
        if subHour(minuts_1,minuts_2):
            hour_Past -= 1
        return (hour_Past,minuts_Past)
    
def subHour (minuts_1,minuts_2):
    if minuts_2 > minuts_1: 
        return False
    else:
        return True

def minutePast(minuts_1, minuts_2):
    if minuts_2 > minuts_1: 
        minuts_Past =  minuts_2 - minuts_1
        return minuts_Past
    else:
        minuts_Past = (60 - minuts_1) + minuts_2
        return minuts_Past

def sameDay(debut, fin):
    if debut < fin:
        return True
    else:
        return False
    