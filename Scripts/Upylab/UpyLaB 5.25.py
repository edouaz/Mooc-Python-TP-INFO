def trace(M):
    if not M:
        return 0
    else:
        add = 0
        for i in range(len(M)):
            add += M[i][i]
        return add