import math
print("[CALCULATEUR DE AIR D'UNE SPHERE EN FONCTION D'UN RAYON]")
r = int(input("Rayon :"))
v =  (4/3)*math.pi*(r**3)
print ("Le volume de la sphére est de :" + str(v))

print()
print("-----------------------------------------------")
print()

print("[CALCULATEUR DE VITTES EN MILES PAR HEURES]")
long = float(input("Longeure parcourus en km : "))
temps = int(input("Temps en secondes : "))
vit = (long/1.61)/((temps/60)/60)
print ("Vitesse en miles par heures : " + str(vit))
ttCN = 3486
print()
print("-----------------------------------------------")
print()
print("[CALCULATEUR D'ARMOIRE EN FCT DU LIVRE RECHERCHE]")
n = int(input("Volume recherché : "))
if (n > ttCN):
    print("Volume invalide le volume " + str(n) + " de Chuck norris n'existe pas n'existe pas !" )
    exit()
r = int(input("Livres par armoirs :"))
arm = n/r

print("Le livre numéro "+ str(n) + " se trouve dans l'armoir " + str(int(arm)))
