def joindre(jointure: str, mots: list[str])->str:
    new = ''
    for i in range(len(mots)):
        if i != len(mots)-1:
            new += mots[i] + jointure
        else:
            new += mots[i]
    return new
        

    


mots = ["Salut", "je programme", "en python"]
print(joindre("--", mots))
