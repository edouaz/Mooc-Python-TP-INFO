
def prime_numbers(nb: int) -> list:
    if type(nb) != int:
        return None
    elif nb < 0:
        return None
    else:
        num = []
        i = 0
        while len(num) <= nb-1:
            i+=1
            if premier(i):
                num.append(int(i))
        return num


    
import math  
def premier(n):
    if n < 2:  
        return False
    for a in range(2, int(math.sqrt(n))+1):
        if(n%a ==0):
            return False
    return True


