def distance_mots(mot_1 : str, mot_2 : str) -> int:
    
    if mot_1 == mot_2:
        return 0
    
    else:
        ## Compteur de lettres différentes
        diff_letters = 0
        ## Pour la longeur du mots
        for i in range(len(mot_1)):
            ## Si la lettre du mots en position i pour le mots 1 et 2 sont différent on ajoute 1 au compteur de lettres différetns
            if mot_1[i] != mot_2[i]:
                diff_letters += 1
        return diff_letters
