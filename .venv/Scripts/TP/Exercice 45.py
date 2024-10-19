import time
def timeit(f, n: int=10000) -> float:
    t1 = time.time()
    i=0
    while i < n:
        f()
        i+=1
    t2 = time.time()
    tt = (t2 - t1) / n
    return tt

def fctcalc():
    i = 0 
    while i < 1000:
        i +=1
    return
print(timeit(fctcalc))
