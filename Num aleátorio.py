#Algoritmo para o usuário tentar acertar qual número o sistema tá pensando 
import random 
import os
#função para limpara tela
def clear():
    os.system('cls')

#Condições para mostrar se a pessoa está colocando um número maior ou menor do número definido, caso esteja correto irá aparecer uma mensagem, casoas tentativas acabem irá aparecer outra mensagem
tentativas = 10
senhaCorrreta = random.randint(1,50)
senha = int(input("Digite um número \n Você tem %s tentativas \n" %tentativas))
tentativas = tentativas - 1
clear()
while senha > senhaCorrreta and tentativas > 0:
    senha = int(input("Digite um número menor \n Você tem %s tentativas \n" %tentativas))
    tentativas = tentativas - 1
    clear()
while senha < senhaCorrreta and tentativas > 0:
    senha = int(input("Digite um número maior \n Você tem %s tentativas \n" %tentativas))
    tentativas = tentativas - 1
    clear()
while senha == senhaCorrreta:
    senha = print("bem vindo playboyzinho") 
while tentativas == 0:
     print("Acabou as tentativas")        
     tentativas = tentativas-1