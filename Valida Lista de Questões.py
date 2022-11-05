def valida_questoes (LQ):
    LP =[]
    for D in LQ:
        DF={}
        TT = True
        TN = True
        TO = True
        TC = True
        if "titulo" not in D:
            DF["titulo"]= "nao_encontrado"
            TT = False
        if "nivel" not in D:
            DF["nivel"]= "nao_encontrado"
            TN = False
        if "opcoes" not in D:
            DF["opcoes"]= "nao_encontrado"
            TO = False
        if "correta" not in D:
            DF["correta"]= "nao_encontrado"
            TC = False
        if len(D)!= 4 :
            DF["outro"]= "numero_chaves_invalido"
        if TT == True:
            if len(D["titulo"])== 0 or D["titulo"].isspace()== True :
                DF["titulo"]= 'vazio'
        if TN == True:
            if D["nivel"]!= "facil" and D["nivel"]!= "medio" and D["nivel"]!= "dificil":
                DF['nivel']= 'valor_errado'    
        if TO == True: 
            if len(D["opcoes"])!= 4   :
                DF["opcoes"]='tamanho_invalido'
        if TO == True: 
            if len(D["opcoes"])== 4 and "A"  not in D["opcoes"] or "B"  not in D["opcoes"] or "C"  not in D["opcoes"] or "D"  not in D["opcoes"] :
                if 'opcoes'not in DF:
                    DF['opcoes']='chave_invalida_ou_nao_encontrada'
    
        if TO == True and "A"  in D["opcoes"] and len(D["opcoes"])== 4 and  D["opcoes"]['A'].isspace() == True :
            if 'opcoes'not in DF:
                DF["opcoes"]= {}
                DF["opcoes"]["A"]='vazia'  
        if TO == True and "B"  in D["opcoes"] and len(D["opcoes"])== 4 and  D["opcoes"]['B'].isspace() == True :
            if 'opcoes'not in DF:
                DF["opcoes"]= {}
                DF["opcoes"]["B"]='vazia'
            else:
                DF["opcoes"]["B"]='vazia'
        if TO == True and "C"  in D["opcoes"] and len(D["opcoes"])== 4 and  D["opcoes"]['C'].isspace() == True :
            if 'opcoes'not in DF:
                DF["opcoes"]= {}
                DF["opcoes"]["C"]='vazia'
            else:
                DF["opcoes"]["C"]='vazia'
        if TO == True and "D"  in D["opcoes"] and len(D["opcoes"])== 4 and  D["opcoes"]['D'].isspace() == True :
            if 'opcoes'not in DF:
                DF["opcoes"]= {}
                DF["opcoes"]["D"]='vazia'
            else:
                DF["opcoes"]["D"]='vazia'

    
        if TC == True and D['correta']!= 'A' and D['correta']!= 'B' and D['correta']!= 'C'  and D['correta']!= 'D':
            DF['correta']= 'valor_errado'
        LP.append(DF)
    return (LP)