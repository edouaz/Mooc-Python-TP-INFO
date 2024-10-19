n = int(input())
if n%2 == 0 :
    print("Erreur nombre paire !")
elif n%2 != 0:
    for  i in range(1,n+1):
        for  p in range(1,n+1):
            if p == i or p == (n-(i-1)):
                print ("O", end = " ")
            else:
                print("X" , end = " ")
        print()

