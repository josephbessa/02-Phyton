#Sistema para caixa eletronico com multiplas opções.
#Variaveis declaradas e imports do programa.
menuA = 0
saldo = 100
import os 
from time import sleep
#Menu principal do sistema.
while menuA == 0:
    menuA = 0
    print("\nBem Vindo")
    print("Escolha uma opção")
    print("\n 1-- Depositar \n 2-- Sacar \n 3-- Pagar Fatura \n 4-- Conferir Saldo \n 5-- Cancelar  \n")
    menu = int(input("Digite sua opção:"))
    os.system('cls')
  
#Caixa de opções para o usuário escolher qual ação irá ser realizada e se ele realmente pode exercutar ela.
    match menu:
        case 1:
            deposito= int(input("Quanto deseja depositar? "))
            saldo = saldo + deposito 
            print ("Seu saldo atual é "  + str(saldo))
            sleep(5)
        case 2:
            sacar= int(input('Quanto deseja sacar? '))  
            if sacar>saldo: 
                print('Saldo insuficiente')  
            else:
                saldo = saldo - sacar
                print("Seu saldo atual é de: "  + str(saldo))  
                sleep(5)
        case 3:
            fatura= int(input('Qual o valor da fatura? '))  
            if fatura>saldo: 
                print('Saldo insuficiente')  
            else:
                saldo = saldo - fatura
                print("Seu saldo atual é de: "  + str(saldo))
                sleep(5)     
        case 4:
            print('Seu saldo é de: '  + str(saldo)) 
            sleep(5)
        case 5:
            print("Operação finalizada com sucesso :)")
            sleep(5)
            menuA=1       
