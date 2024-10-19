def est_adn(chaine: str) -> bool:
    if not chaine:
        return False
    
    for i in chaine:
        if i not in ["A", "C","G","T"]:
            return False
    return True

