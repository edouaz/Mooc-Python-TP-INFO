import math 
def catalan(n):
    r = (math.factorial(2*n)) /   ((math.factorial(n+1)) * (math.factorial(n)))
    return int(r)
