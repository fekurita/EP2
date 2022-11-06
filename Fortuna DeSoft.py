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
                    if id<3:
                        nivel = "facil"
                    elif id>3 and id<7:
                        nivel = "medio"
                    else:
                        nivel = "dificil"
                    print('\n''\n')
                    questaoatual = sorteia_questao_inedida(Questoespn,nivel,Questoesusa)
                    print(questao_para_texto(questaoatual,id))
                    resposta = input('\n'"Qual sua resposta?!")
                    if resposta == questaoatual["correta"]:
                        print ("Você acertou! Seu prêmio atula é de R$ {}".format(Lpremio[id-1]))
                        if id ==3:
                            print("HEY! Você passou para o Nível MEDIO!")
                        if id == 6:
                            print("HEY! Você passou para o Nível DIFICIL!")
                        id +=1
                        while T4 == True:
                            Continuarfinal = input("Aperte ENTER para continuar...")
                            if Continuarfinal == "":
                                T4 = False
                            else:
                                Continuarfinal =input("Aperte ENTER para continuar...")
                    else: 
                        print ("Que pena! Você errou e vai sair sem nada :(") 
                        T3 = False


            else:
                Continuar =input("Aperte ENTER para continuar...")

    else:
        Comeco =input("Aperte ENTER para continuar...") 


