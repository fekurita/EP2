from funcoes import *
from Questoes import *

Questoespn =transforma_base(quest)
Questoesusa =[]

id = 1
Lpremio=[0.00,1000.00,5000.00,10000.00,30000.00,50000.00,100000.00,300000.00,500000.00,1000000.00]

print ("Olá! Você está na Fortuna DeSoft e terá a oportunidade de enriquecer!"'\n')
Nome =input("Qual seu nome?")
print('\n'"Ok {0}, você tem direito a pular 3 vezes e 2 ajudas!"'\n'"As opções de resposta são A, B, C, D, ajuda, pula e parar!"'\n'.format(Nome.upper()))
Comeco =input("Aperte ENTER para continuar...")

T = True
T2 = True
T3 = True
T4 = True
T5 = True

modorepete = False

Avisafinal = False

Questaosalva= ""

Pulos = 3
Ajudas = 2
while T == True:
    if Comeco == '':
        T = False
        print ( '\n'"O jogo já vai começar! Lá vem a Primeira questão"'\n')
        Continuar =input("Vamos começar com questões do nível FACIL!"'\n'"Aperte ENTER para continuar...")
        while T2 == True:
            if Continuar =="":
                T2 = False
                while T3 == True and id<10:
                    T4=True
                    Avisafinal = False
                    if id<=3:
                        nivel = "facil"
                    elif id>3 and id<7:
                        nivel = "medio"
                    else:
                        nivel = "dificil"
                    print('\n''\n')
                    if modorepete == False :
                        questaoatual = sorteia_questao_inedida(Questoespn,nivel,Questoesusa)
                        questaoatualtexto = questao_para_texto(questaoatual,id)
                    print(questaoatualtexto)
                    resposta = input('\n'"Qual sua resposta?!")
                    while resposta != "A"and resposta != "B"and resposta != "C"and resposta != "D"and  resposta != "ajuda"and resposta != "pula"and resposta != "parar":
                        print("Opção inválida!"'\n'"As opções de resposta são  A, B, C, D, ajuda, pula e parar!")
                        resposta = input('\n'"Qual sua resposta?!")
                    if resposta == questaoatual["correta"] and id<=9:
                        modorepete = False
                        print ("Você acertou! Seu prêmio atula é de R$ {}".format(Lpremio[id]))
                        if id ==3:
                            print('\n'"HEY! Você passou para o Nível MEDIO!")
                        if id == 6:
                            print('\n'"HEY! Você passou para o Nível DIFICIL!")
                        id +=1
                
                        while T4 == True and id<10:
                            Continuarfinal = input("Aperte ENTER para continuar...")
                            if Continuarfinal == "":
                                T4 = False
                            else:
                                Continuarfinal =input("Aperte ENTER para continuar...")
                    if resposta == questaoatual["correta"] and id==10:
                        print("PARABÉNS, você zerou o jogo e ganhou um milhão de reais")
                        jogardnv = input("Gostaria de jogar de novo [S/N]?")
                        while jogardnv != "S" and jogardnv != "N":
                            print("Opção inválida!")
                            jogardnv = input("Gostaria de jogar de novo [S/N]?")
                        if jogardnv == "S":
                            id = 1
                        if jogardnv == "N":
                            T3 = False
                        print("Jogo encerrado")   
                    if resposta == "pula" and Pulos>0:
                        Avisafinal = True
                        T5 = True
                        Pulos-=1
                        if Pulos>=1:
                            print("Ok pulando! Você ainda tem {0} pulos!".format(Pulos))
                        else:
                            print("Ok pulando! Você não tem mais direito a pulos!")
                        while T5 == True:
                            Continuarpulos = input("Aperte ENTER para continuar...")
                            if Continuarpulos == "":
                                T5 = False
                            else:
                                Continuarpulos = input("Aperte ENTER para continuar...")
                    if resposta == "pula" and Pulos == 0:
                        Avisafinal = True
                        T5 = True
                        T4 = True
                        print("Não deu! Você não tem mais direito a pulos")
                        while T5 == True:
                            Continuarpulos = input("Aperte ENTER para continuar...")
                            if Continuarpulos == "":
                                T5 = False
                            else:
                                Continuarpulos = input("Aperte ENTER para continuar...")
                        modorepete = True
                    if resposta == "ajuda" and Ajudas>0:
                        T5 = True
                        Avisafinal = True
                        modorepete = True
                         
                        if Questaosalva == "" or Questaosalva!= questaoatual:
                            if Ajudas == 2 :
                                print("Ok, lá vem ajuda! Você ainda tem 1 ajudas"'\n')
                            if Ajudas == 1 :
                                print("Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!"'\n') 
                            while T5 == True:
                                Continuarajuda = input("Aperte ENTER para continuar...")
                                if Continuarajuda == "":
                                    T5 = False
                                else:
                                    Continuarajuda = input("Aperte ENTER para continuar...")

                            print(gera_ajuda(questaoatual))
                        else:
                            print("Não deu! Você já pediu ajuda nesta questão!")
                        T5 = True
                        while T5 == True:
                            Continuarajuda = input("Aperte ENTER para continuar...")
                            if Continuarajuda == "":
                                T5 = False
                            else:
                                Continuarajuda = input("Aperte ENTER para continuar...")

                        Questaosalva = questaoatual
                    if resposta == "ajuda" and Ajudas ==0:
                        Avisafinal = True
                        T5 = True
                        T4 = True
                        print("Não deu! Você não tem mais direito a ajuda!")
                        while T5 == True:
                            Continuarpulos = input("Aperte ENTER para continuar...")
                            if Continuarpulos == "":
                                T5 = False
                            else:
                                Continuarpulos = input("Aperte ENTER para continuar...")
                        modorepete = True
                    if resposta == "parar":
                        Avisafinal = True
                        Sair = input('\n'"Deseja mesmo parar [S/N]? Caso responda  S, sairá com R$ {0} ".format(Lpremio[id-1]))
                        while Sair != "S" and Sair != "N":
                            print("Opção inválida!")
                            Sair = input('\n'"Deseja mesmo parar [S/N]? Caso responda  S, sairá com R$ {0} ".format(Lpremio[id-1]))
                        if Sair == "S":
                            print('\n'"Ok! Você parou e seu prêmio é de R$ {0}".format(Lpremio[id-1]))
                            jogardnv = input("Gostaria de jogar de novo [S/N]?")
                            while jogardnv != "S" and jogardnv != "N":
                                print("Opção inválida!")
                                jogardnv = input("Gostaria de jogar de novo [S/N]?")
                                if jogardnv == "S":
                                    id = 1
                                    Questoesusa =[]
                                if jogardnv == "N":
                                    T3 = False
                            print("Jogo encerrado")
                        if Sair == "N":
                            modorepete=True

                    if resposta != questaoatual["correta"] and Avisafinal==False: 
                        print ("Que pena! Você errou e vai sair sem nada :(") 
                        jogardnv = input("Gostaria de jogar de novo [S/N]?")
                        while jogardnv != "S" and jogardnv != "N":
                            print("Opção inválida!")
                            jogardnv = input("Gostaria de jogar de novo [S/N]?")
                        if jogardnv == "S":
                            id = 1
                            Questoesusa =[]
                        if jogardnv == "N":
                            T3 = False
                            print("Jogo encerrado")
            else:
                Continuar =input("Aperte ENTER para continuar...")
    else:
        Comeco =input("Aperte ENTER para continuar...") 