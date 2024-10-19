
def my_insert(list : list, n : int) -> list:
    ## On regarde si x est soit un float ou un int 
    x = isinstance(n, (float, int))
    ## Si ce n'est pas un float ou un int on retourne une erreur
    if not(x):
        return 'AssertionError'
    
    ## Ajoute n a la liste
    list.append(n)
    ## Trie la liste 
    list.sort()
    
    
