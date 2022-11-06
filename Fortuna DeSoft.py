from funcoes import *
from Questoes import *

Questoespn =transforma_base(quest)
Questoesusa =[]

id = 1
Lpremio=[1000,5000,10000,30000,50000,100000,300000,500000,1000000]

print ("Olá! Você está na Fortuna DeSoft e terá a oportunidade de enriquecer!"'\n')
Nome =input("Qual seu nome?")
print('\n'"Ok {0}, você tem direito a pular 3 vezes e 2 ajudas!"'\n'"As opções de resposta são A, B, C, D, ajuda, pula e parar!"'\n'.format(Nome.upper()))
Comeco =input("Aperte ENTER para continuar...")

T = True
T2 = True
T3 = True
T4 = True
T5 = True

modopulo = False

Avisapulo = False

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
                    Avisapulo = False
                    if id<3:
                        nivel = "facil"
                    elif id>3 and id<7:
                        nivel = "medio"
                    else:
                        nivel = "dificil"
                    print('\n''\n')
                    if modopulo == False :
                        questaoatual = sorteia_questao_inedida(Questoespn,nivel,Questoesusa)
                        questaoatualtexto = questao_para_texto(questaoatual,id)
                    print(questaoatualtexto)
                    resposta = input('\n'"Qual sua resposta?!")
                    if resposta == questaoatual["correta"]:
                        modopulo = False
                        print ("Você acertou! Seu prêmio atula é de R$ {}".format(Lpremio[id-1]))
                        if id ==3:
                            print("HEY! Você passou para o Nível MEDIO!")
                        if id == 6:
                            print("HEY! Você passou para o Nível DIFICIL!")
                        id +=1
                        if id ==10 :
                            print("PARABÉNS, você zerou o jogo e ganhou um milhão de reais")
                        while T4 == True and id<10:
                            Continuarfinal = input("Aperte ENTER para continuar...")
                            if Continuarfinal == "":
                                T4 = False
                            else:
                                Continuarfinal =input("Aperte ENTER para continuar...")
                    if resposta == "pula" and Pulos>0:
                        Avisapulo = True
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
                        Avisapulo = True
                        T5 = True
                        T4 = True
                        print("Não deu! Você não tem mais direito a pulos")
                        while T5 == True:
                            Continuarpulos = input("Aperte ENTER para continuar...")
                            if Continuarpulos == "":
                                T5 = False
                            else:
                                Continuarpulos = input("Aperte ENTER para continuar...")
                        modopulo = True



                    if resposta != questaoatual["correta"] and Avisapulo==False: 
                        print ("Que pena! Você errou e vai sair sem nada :(") 
                        T3 = False


            else:
                Continuar =input("Aperte ENTER para continuar...")

    else:
        Comeco =input("Aperte ENTER para continuar...") 


