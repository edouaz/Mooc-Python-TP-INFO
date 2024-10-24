
# Compacte 
def inventaire(offres, objets):
    return {offres[obj] for obj in objets if obj in offres}


## version etandue du scripte : 

def inventaire(offres, objets):
    
    result = {}  
    for obj in objets:  
        if obj in offres: 
            result[obj] = offres[obj]  
    return result 
