import random
NB_ESSAIS_MAX = 6
NB_ESSAIS = 0
n =0 
secret = random.randint(0, 100)
for i in range(NB_ESSAIS_MAX):
    n = int(input())
    NB_ESSAIS += 1
    
    if n == secret:
        print("Gagné en" , NB_ESSAIS , "essai(s) !")
        break
    elif n > secret and NB_ESSAIS < NB_ESSAIS_MAX:
        print("Trop grand")
    elif n < secret and NB_ESSAIS < NB_ESSAIS_MAX:
        print("Trop petit")
        
if n != secret: 
    print("Perdu ! Le secret était", secret)       

