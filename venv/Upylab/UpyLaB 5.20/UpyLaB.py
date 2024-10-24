def nouveaux_heros(hist, new_hist) :
    # On ouvre de maniére sécuriser le fichier en mode read
    with open(hist, "r", encoding="utf-8")  as mon_fichier :
        # On ouvre de maniére sécuriser le ficher en mode write
        with open(new_hist, "w", encoding="utf-8") as new_fichier:
            # Pour chaque linges 
            for line in mon_fichier:
                # On regrade ci un des elements est remplacable par le nouveau nom
                line = line.replace("Paul", "Tom")
                line = line.replace("Pierre", "Paul")
                line = line.replace("Jacqueline", "Mathilde")
                new_fichier.write(line) # On réecrit sur notre nouveau ficher 