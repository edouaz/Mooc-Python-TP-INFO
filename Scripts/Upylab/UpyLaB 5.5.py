def longueur(*points):
    seg_total = 0 
    for i in range(0,len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        seg_total += ((((x1 - x2)**2) + ((y1 - y2)**2))**(1/2))
    return seg_total

    