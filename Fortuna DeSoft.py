print ("Olá! Você está na Fortuna DeSoft e terá a oportunidade de enriquecer!"'\n')
Nome =input("Qual seu nome?")
print('\n'"Ok {0}, você tem direito a pular 3 vezes e 2 ajudas!"'\n'"As opções de resposta são A, B, C, D, ajuda, pula e parar!"'\n'.format(Nome.upper()))
Comeco =input("Aperte ENTER para continuar...")

T = True
T2 = True
while T == True:
    if Comeco == '':
        T = False
        print ( '\n'"O jogo já vai começar! Lá vem a Primeira questão"'\n')
        Continuar =input("Vamos começar com questões do nível FACIL!"'\n'"Aperte ENTER para continuar...")
        while T2 == True:
            if Continuar =="":
                T2 = False
                
            else:
                Continuar =input("Aperte ENTER para continuar...")

    else:
        Comeco =input("Aperte ENTER para continuar...") 


