def to_float(s):
    if s.split('.'):
        ent,dec = s.split('.')
        for i in ent,dec:
            if not(i.isdigit()):
                return None
        return s
    else:
        return None
    
print(to_float("0848.115088"))