def decompresse (t):
    # avec les compréhension
    n_list = [t[i][1] for i in range(len(t)) for r in range(t[i][0])  ]
    return n_list
    
    # Voici comment j'aurais fait sans les compréhension
    t_list = []
    for i in range(len(t)):
        for r in range(t[i][0]):
            t_list.append(t[i][1])
