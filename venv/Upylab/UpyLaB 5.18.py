def my_filter(lst : list, f ) -> list:
    # On crée une nouvelle liste en filtrant seulement les éléments de lst
    # Si la fonction f(x) renvoie True, on garde x dans la liste, sinon on l'éjecte
    list_r = [x for x in lst if f(x)]
    return list_r  # On renvoie la nouvelle liste filtrée

def is_int(x):
    # On vérifie si x est un entier
    return isinstance(x, int)

# On teste le tout avec une liste random d'éléments
# Ici on cherche juste les entiers : 666, 42 et on ignore les strings et float
print(my_filter(['hello', 666, 42, 'Thierry', 1.5], is_int))


# Version bonus : on peut faire ça en utilisant lambda pour rendre le code plus compact
# lambda c’est juste une façon d’écrire une fonction rapide et pas forcément hyper lisible
# Tu remplaces is_int par lambda x : isinstance(x, int) direct dans l'appel de my_filter
# Perso, je trouve ça moins clean, mais à toi de voir 
