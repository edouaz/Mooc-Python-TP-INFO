def symetrie_horizontale(A):
    if not A:
        return []
    
    sym_mat = []
    for i in range(len(A)):
        sym_mat.append(A[len(A) - i - 1])