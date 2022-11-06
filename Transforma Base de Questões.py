def transforma_base (L):
    DF={}
    for D in L:
        if D["nivel"] not in DF:
            DF[D["nivel"]]=[D]
        else:
            DF[D["nivel"]].append(D)
    return DF    
