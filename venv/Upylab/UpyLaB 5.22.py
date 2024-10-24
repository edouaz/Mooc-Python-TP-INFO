def wc(nomFichier):
    chars = 0  # Compte des caractères
    words = 0  # Compte des mots
    lines = 0  # Compte des lignes

    # On ouvre le fichier en mode lecture avec encodage UTF-8
    with open(nomFichier, 'r', encoding='utf-8') as mon_fichier:
        # On parcourt chaque ligne du fichier
        for line in mon_fichier:
            lines += 1  # Incrémentation du compteur de lignes
            chars += len(line)  # On compte tous les caractères de la ligne, y compris les espaces et '\n'
            
            current_word = ''  # Pour accumuler les caractères alphanumériques

            # Parcours caractère par caractère dans chaque ligne
            for char in line:
                if char.isalnum():  # Si le caractère est alphanumérique, il fait partie d'un mot
                    current_word += char
                else:  # Si on rencontre un séparateur (espace, ponctuation, etc.)
                    if current_word:  # Si un mot a été accumulé
                        words += 1  # On incrémente le compteur de mots
                        current_word = ''  # On réinitialise pour le prochain mot

            # Vérification de fin de ligne si un mot est resté en cours
            if current_word:
                words += 1

    return chars, words, lines  # Retourne un tuple avec (caractères, mots, lignes)

# Exemple d'appel de la fonction (vous pouvez remplacer par les fichiers UpyLaB)
print(wc("/home/edouard/Documents/BA1 - INFO/Phyton project test/INFO-F101/venv/Upylab/UpyLaB 5.19/Apollinaire.txt"))
