def construction_dict_amis(list_prenom):
    dir_ret = {}  # Dictionnaire pour stocker les amis
    
    # Parcourir chaque couple de prénoms dans la liste
    for prenom1, prenom2 in list_prenom:
        # Ajouter prenom1 au dictionnaire s'il n'est pas déjà présent
        if prenom1 not in dir_ret:
            dir_ret[prenom1] = set()  # Initialiser avec un ensemble vide
        
        # Ajouter prenom2 à l'ensemble des amis de prenom1
        dir_ret[prenom1].add(prenom2)

        # Ajouter prenom2 au dictionnaire s'il n'est pas déjà présent
        if prenom2 not in dir_ret:
            dir_ret[prenom2] = set()  # Initialiser avec un ensemble vide

    return dir_ret

# Exemple d'appel
print(construction_dict_amis([('Quidam', 'Pierre'),
                         ('Thierry', 'Michelle'),
                         ('Thierry', 'Pierre')]))
