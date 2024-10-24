def acrostiche(fichier) -> str:
    # On crée une liste vide pour stocker la première lettre de chaque ligne
    start_letter = []
    
    # On ouvre le fichier en mode lecture ('read') avec le bon encodage
    # 'with' c'est pratique car ça ferme automatiquement le fichier après utilisation
    with open(fichier, encoding="utf-8") as mon_fichier:
        # On parcourt chaque ligne du fichier (chaque 'm' représente une ligne)
        for m in mon_fichier:
            # On ajoute la première lettre de chaque ligne dans la liste 'start_letter'
            start_letter.append(m[0])
    
    # Maintenant on convertit la liste en une seule chaîne de caractères
    # '.join()' permet de coller les lettres ensemble sans espace entre elles
    return ''.join(start_letter)
