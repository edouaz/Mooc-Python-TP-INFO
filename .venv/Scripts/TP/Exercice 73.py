
l = ["Salut", "comment", "ça", "va?"]

def enumerer(liste):
    n = []
    for i in range(len(liste)):
        n.append((i, liste[i]))
    return n
    
    


for i, element in enumerer(l):
    print(i, element)