x = float(input())
tem = x
sin_x = 0.0
e = 10**(-6)
n = 1
s = 1
while abs(tem) > e:
    sin_x += tem
    n +=2
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    tem = (-1)**s * (x**n) / fact
    s +=1

print (sin_x)
