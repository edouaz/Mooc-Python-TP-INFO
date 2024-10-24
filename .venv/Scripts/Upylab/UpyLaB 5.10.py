def dupliques( sequance ) -> bool:
    
    same_obj = 0
    ## Pour chaque obj dans sequance 
    for obj in sequance:
        ## Pour chaque character dans sequance 
        for pos in range(len(sequance)):
            ## Si il y a un charactére qui est identique on ajoute +1
            if obj == sequance[pos]:
                same_obj += 1
    ## Si same obj est aussi long que la sequance c'est qu'il n'y a pas de doublons 
    if same_obj == len(sequance):
        return False
    else :
        return True

