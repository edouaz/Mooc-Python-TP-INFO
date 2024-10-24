def print_mat(M):
    if not M:
        print("")
    for i in M:
        for r in i:
            print(r, end=' ')
        print()


ma_matrice = eval(input())
print_mat(ma_matrice)