def plus_grand_bord(w):
    
    for i in range(1, len(w)):
        
        if w[:i] == w[-i:]:
            plus_grand = w[:i]  

    return plus_grand if 'plus_grand' in locals() else ""