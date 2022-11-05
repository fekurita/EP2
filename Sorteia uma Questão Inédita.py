import random

def sorteia_questao_inedida (D,N,LS):
    T = True
    while T == True:   
        Q = random.choice(D[N])
        if Q not in LS:
            T = False
            LS.append(Q)
    return (Q)