import random
s = int(input())
random.seed(s)

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

points = 0

coup_j = str
coup_o = str

def bat(joueur_1: int, joueur_2: int):

    if(joueur_1 == PIERRE and joueur_2 == PIERRE):
        return None
    elif(joueur_1 == PIERRE and joueur_2 == FEUILLE):
        return False
    elif(joueur_1 == PIERRE and joueur_2 == CISEAUX):
        return True
    elif(joueur_1 == FEUILLE and joueur_2 == PIERRE):
        return True
    elif(joueur_1 == FEUILLE and joueur_2 ==FEUILLE):
        return None
    elif(joueur_1 == FEUILLE and joueur_2 == CISEAUX):
        return False
    elif(joueur_1 == CISEAUX and joueur_2 == PIERRE):
        return False
    elif(joueur_1 == CISEAUX and joueur_2 == FEUILLE):
        return True
    elif(joueur_1 == CISEAUX and joueur_2 ==CISEAUX):
        return None

def manche(points):
    j1 = int(input())
    o1 = random.randint(0,2)
    gagant = bat(j1,o1)
    coup_j = coupToSting(j1)
    coup_o = coupToSting(o1)
    if(gagant == True):
        points += 1 
        print(coup_o , "est battu par", coup_j , ":",points)
        
        return points
    elif(gagant == False):
        points -= 1 
        print(coup_o , "bat", coup_j , ":",points)
        
        return  points
    elif(gagant == None):
        print(coup_o , "annule" , coup_j , ":", points)
        return points

def coupToSting(j):
    if j == PIERRE:
        return "Pierre"
    elif j == FEUILLE:
        return "Feuille"
    elif j == CISEAUX:
        return "Ciseaux"
    

for i in range(5):
    points = manche(points)

if(points > 0):
    print("Gagné")
elif(points < 0 ):
    print("Perdu")
elif(points == 0):
    print("Nul")
    
    



