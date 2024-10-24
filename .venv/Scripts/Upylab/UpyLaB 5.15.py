

def correcteur(mot : str, liste_mots : list) -> str:
    possible_words = []
    ## Regarde les mots qui ont la même longeurs 
    for i in range(len(liste_mots)):
        if len(mot) == len(liste_mots[i]):
            possible_words.append(liste_mots[i])
    
    ## Regarder parmis mots de la méme longeur le quel a une seul lettre de différence
    for j in range(len(possible_words)):
        diff_letters = 0
        ## Pour la longeur du mots
        for x in range(len(mot)):
            ## Si la lettre du mots en position i pour le mots 1 et 2 sont différent on ajoute 1 au compteur de lettres différetns
            if mot[x] != possible_words[j][x]:
                diff_letters += 1
        ## Si il y a moin ou une lettre de diff on retourne le mot
        if diff_letters <= 1:
            return possible_words[j]


