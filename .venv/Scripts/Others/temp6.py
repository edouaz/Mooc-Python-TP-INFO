def signature(nom_prenom):
    nom = nom_prenom[0]  # nom
    prenom = nom_prenom[1]  # prénom
    prenom_nom = prenom + ' ' + nom  # ajout de l'espace entre prénom et nom
    return prenom_nom
