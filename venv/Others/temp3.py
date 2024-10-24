x = float(input())
sin_x = 0.0
tem = x
n = 1
epsilon = 10**-6

while abs(tem) > epsilon:
    sin_x +=tem
    n +=2
    tem = (-tem * x **2) / (n * (n - 1))
    
print(sin_x)