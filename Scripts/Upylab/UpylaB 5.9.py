def anagrammes(word_1 : str, word_2 : str) -> bool:
    '''Chek si deux mots son des anagrames'''
    ## Si la longeurs des mots est différentes on retourne Fales et la fct s'arrete
    if len(word_2) != len(word_1):
        return False
    
    ## On regarde combien de lettres différentes il y a dans le mots
    seen_letters = []
    for r in range(len(word_1)):
        if word_1[r] not in seen_letters:
            seen_letters.append(word_1[r])
    ## On fait une liste que l'on va augmanter quand on rencontre une lettre dans les deux mots
    same_caracter_needed_for_anagramme = 0
    ## Une permier boucle pour regarder chaque diférants caractére de notre liste seen_letters
    for letter in seen_letters:
        ## Une boucle pour regarder a chaque lettres de notres mot 
        for j in range(len(word_1)):
            ## Si la lettre de seen_letters est égale a la lettre de word_2 en [j] on ajoute +1 a same_caracter... (j'aurrais aussi pu directement faire que j = la lettre de word_1)
            if letter == word_2[j]:
                same_caracter_needed_for_anagramme +=1
    ## Après avoir regarder toutes le lettres et conter les lettre qui sont identique on re vérifie si elles sont = a la longeurs d'un des mots puis on retourne si oui
    if same_caracter_needed_for_anagramme == len(word_1):
        return True
    else:
        return False
    

print(anagrammes('pate', 'patte'))