def liste_des_mots(fichier : str) -> list:
    character_list = []
    caracteres_undesirables = '!@#$%^&*()-=+{}[]:;"\'<>,.?/\\~°§0123456789'
    with open(fichier, "r", encoding="utf-8") as mon_fichier:
        lines = mon_fichier.read()
        
    for caracteres in caracteres_undesirables:
        lines = lines.replace(caracteres, ' ')
    words = lines.lower().split()
    character_list = sorted(set(words))
    return character_list
