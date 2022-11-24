'''Nome: Joseph Bessa
Programa para auxiliar o usuário o que fazer em sua folgadando 3 opções: Pedir um ifood e ficar em casa, ir ao cinema e ir aoestádio e ver um jogo da copa do mundo
 '''
 #Declaração de váriavel para o while pro clear
menuA = 0 
import os

def clear():
    os.system('cls')
#Tela de acolhimentodo programa
name = input("Digite seu nome \n")  
clear()  
print("O que deseja fazer em sua folga %s? \n" %name)
#Menu criado com opções e resultados para cada escolha feita
while menuA == 0:
    menuA = 0
    print("Escolha o que quer fazer: \n 1 - Pedir um ifood \n 2 - Ir ao cinema \n 3 - Ver um jogo de futebol ")
    menu = int(input("Digite uma opção (números):"))
    clear()

    match menu:
            case 1:
                print("1 - 25 salgados variados (R$ 15,00) \n 2 - Hambúrguer (R$ 20,00) \n 3 - Pizza Gigante de Calabresa (R$ 45,00) \n")
                menuFood = int(input("Digite uma opção (números):"))
                match menuFood:
                    case 1:
                        qtde = int(input("\n Você deseja comprar quantos combos de salgados?"))
                        value = 15 * qtde
                        print("O valor da sua compra é de: "  + str(value), "reais")
                    case 2:
                        qtde = int(input("\n Você deseja comprar quantos hambúrgueres?"))
                        value = 20 * qtde
                        print("O valor da sua compra é de: "  + str(value), "reais")
                    case 3:
                        qtde = int(input("\n Você deseja comprar quantas pizzas?"))
                        value = 45 * qtde
                        print("O valor da sua compra é de: "  + str(value), "reais") 
                        menuA=1       
            case 2:
                print("O valor do ingresso é de: 24 reais \n")
                print("Você quer ver qual filme: \n 1 - Pantera Negra \n 2 - Adão Negro \n 3 - Mundo Estranho \n") 
                menuFilm = int(input("Digite uma opção (números): \n"))
                match menuFilm:
                    case 1:
                        print("Ingresso para Pantera Negra comprado com sucesso, bom filme :) ")
                    case 2:
                        print("Ingresso para Adão Negro comprado com sucesso, bom filme :) ")
                    case 3:
                        print("Ingresso para Mundo Estranho comprado com sucesso, bom filme :) ") 
                        menuA=1 
            case 3: 
                print("Você deseja ver qual jogo? \n")
                print("1 - Brasil x Sérvia (R$ 1.200,00) \n 2 - Alemanha x Espanha (R$ 1.150,00) \n 3 - Portugal x Uruguai (R$ 1.000,00) \n") 
                menuFootball = int(input("Digite uma opção (números):"))
                match menuFootball:
                    case 1:
                        print("Ingresso comprado, VAI BRASIIIL")
                    case 2:
                        print("Ingresso comprado, bom jogo :)")    
                    case 3:
                        print("Ingresso comprado, SIIUU")
                        menuA=1 
            case _:
                print("Opção invalída")  
                menuA=0           
#Finalização do programa caso tenha feito umaescolha válida.


