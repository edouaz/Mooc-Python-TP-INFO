def intersection(word_1 : str, word_2 : str) -> str:
    
    ## Liste des partie qui sont dans les deux mots 
    same_character = []
    ## Premiére boucle pour savoir a partire de ou on va commencer a regarder pour des str similaire (pos de départ)
    for start in range(len(word_1)):
        ## Deuxsiéme boucle pour savoir ou on va finir de regarder les str similaire (pos de fin)
        ## On dois ajouter +1 si non on ne séléctionne auccun caractére et ca pause probléme 
        for end in range(start + 1, len(word_1) + 1):

            sous_str = word_1[start:end]
            ## Si on trouve un str similaire on l'ajoute a same_character 
            if word_2.find(sous_str) != -1:
                same_character.append(sous_str)
    
    ## Si same_character n'est pas vide 
    if same_character: 
        ## J'ai été voir sur stackoverflow pour faire ca car si non on devais faire encore une bloucle et c'est pas fou 
        ## On retourne la plus longe chaine de charactér
        return max(same_character, key=len)
    else:
        return '' 

    
