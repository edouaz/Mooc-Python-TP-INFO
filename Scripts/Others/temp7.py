c_adn = ("A", "C", "T", "G")

def est_adn(ADN):
    for i in range(len(ADN)):
        if ADN[i] not in c_adn:  
            return False
    return True

