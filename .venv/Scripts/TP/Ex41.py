

def faco(n):
    p = 1
    for i in range(n):
        p = p*i

def Bell (n):
    if n == 0 :
        return 1
    else:
        som_1 = 0
        for k in range(1,n+1):
            som_1 = 1/faco(k)
            som_2 = 0
            for i in range(1,k):
                x = (-1)**(k-i)


        


