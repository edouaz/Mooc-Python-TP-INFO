

def plus_grand_bord(w):
    
    for i in range(1, len(w)):
        if w[:i] == w[-i:]:
            return w[:i]
    return ''

