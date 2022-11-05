import random

def gera_ajuda (Q):
    LIC = []
    LI = []
    for L,que in Q["opcoes"].items():
        if L not in Q["correta"]:
            LIC.append(que)
    i = 0
    N = random.randint(1,2)
    while i<N:
        QI = random.choice(LIC)
        LI.append(QI)
        LIC.remove(QI)
        i+=1
    if N == 1:
        return("DICA:"
        '\n'
        "Opções certamente erradas: {0}"
        ).format(LI[0])
    else:
        return("DICA:"
        '\n'
        "Opções certamente erradas: {0} | {1}"
        ).format(LI[0],LI[1])  