def questao_para_texto (D,ID):
    return ("----------------------------------------"
    '\n'
    "QUESTAO {0}"
    '\n'
    '\n'
    "{1}"
    '\n'
    '\n'
    "RESPOSTAS:"
    '\n'
    "A: {2}"
    '\n'
    "B: {3}"
    '\n'
    "C: {4}"
    '\n'
    "D: {5}"
    ).format(ID,D["titulo"],D["opcoes"]["A"],D["opcoes"]["B"],D["opcoes"]["C"],D["opcoes"]["D"])