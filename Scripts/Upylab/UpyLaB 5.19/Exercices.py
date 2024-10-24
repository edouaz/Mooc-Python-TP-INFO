import os

def acrostiche(fichier) -> str:
    # On récupère le dossier où se trouve le script actuel (très utile dans VS Code)
    script_dir = os.path.dirname(__file__)
    
    # On crée le chemin complet vers le fichier, en supposant qu'il est dans le même dossier
    fichier_path = os.path.join(script_dir, fichier)
    
    # Liste vide pour stocker la première lettre de chaque ligne
    start_letter = []
    
    # On ouvre le fichier (en utilisant son chemin complet) et on le lit ligne par ligne
    with open(fichier_path, encoding="utf-8") as mon_fichier:
        # Pour chaque ligne du fichier, on récupère la première lettre
        for m in mon_fichier:
            start_letter.append(m[0])  # On ajoute la première lettre à la liste
    
    # On retourne toutes les lettres collées en une seule chaîne de caractères
    return ''.join(start_letter)

# Test du code, ici tu mets juste le nom du fichier s'il est dans le même dossier que ton script
print(acrostiche('Apollinaire.txt'))
