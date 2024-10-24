def my_pow(m: int, b: float):
    # Vérification des types
    if isinstance(m, int) and isinstance(b, float):
        # on génére les m premier nombre avec de b**i
        return [b**i for i in range(m)]
    else:
        return None
    
