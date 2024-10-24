# On fait un petit compteur de mots 
words_count = 0

# Petite fonction pour compter les lettres, on prend deux paramètres : une minuscule et une majuscule
def count_letter(letter_min: str, letter_maj) -> list:
    list_of_e = []  # Ici, on va stocker tous les mots qui contiennent la lettre en question
    count = 0  # Variable pour compter le nombre total de mots dans le fichier

    with open("/home/edouard/Documents/BA1 - INFO/Phyton project test/INFO-F101/venv/Upylab/Mooc 5.8.4/words.txt", encoding="utf-8") as mon_fichier:
        # On passe en revue chaque mot du fichier
        for m in mon_fichier:
            # Si la lettre (min ou maj) est dans le mot, on l'ajoute à la liste
            if letter_min in m or letter_maj in m:
                list_of_e.append(m.strip())  # strip() c'est pour enlever les espaces en trop
            count += 1  # On garde le compte du nombre total de mots

    return list_of_e, count  # On renvoie la liste et le total de mots

# On appelle la fonction pour choper les mots avec "e" ou "E"
e_list, words_count = count_letter("e", "E")

# On affiche la liste des mots trouvés
print(e_list)

# Et là, on calcule la proportion de mots qui contiennent la lettre "e"
print(len(e_list) / words_count)
