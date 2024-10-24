def calcul_prix(produits, catalogue):
    panier = 0
    for p in produits:
        if p in catalogue:
            n_fois = produits[p]
            panier += catalogue[p] * n_fois
    return panier

