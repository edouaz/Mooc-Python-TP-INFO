def top_3_candidats(moyennes):
    top1_moy = 0
    top2_moy = 0
    top3_moy = 0
    top1_name = ""
    top2_name = ""
    top3_name = ""
    for cand, moy in moyennes.items():
        if moy > top1_moy:
            top3_moy = top2_moy
            top3_name = top2_name
            top2_moy = top1_moy
            top2_name = top1_name
            top1_moy = moy
            top1_name = cand
        elif moy > top2_moy:
            top3_moy = top2_moy
            top3_name = top2_name
            top2_moy = moy
            top2_name = cand
        elif moy > top3_moy:
            top3_moy = moy
            top3_name = cand

    ret_tupl = (top1_name, top2_name, top3_name)
    return ret_tupl

