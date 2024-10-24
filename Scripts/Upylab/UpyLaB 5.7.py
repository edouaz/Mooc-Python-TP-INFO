def plus_grand_bord(w):
    # On parcourt chaque indice i à partir de 1 jusqu'à la longueur de la chaîne w
    for i in range(1, len(w)):
        # On vérifie si la sous-chaîne du début de la longueur i est égale
        # à la sous-chaîne de la fin de la longueur i
        if w[:i] == w[-i:]:
            # Si c'est le cas, on enregistre cette sous-chaîne dans la variable plus_grand
            plus_grand = w[:i]  

    # On retourne la plus grande sous-chaîne trouvée si elle existe,
    # sinon on retourne une chaîne vide
    return plus_grand if 'plus_grand' in locals() else ""
