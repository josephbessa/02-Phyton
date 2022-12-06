menuB = 1
num1 = []
par = 0
impar = 0
#Importação de bibliotecas 
import os
import statistics
import random
#Criação de um menu funcional para acessar outras funções do programa
while menuB == 1:
    menuA = int(input("Lista de Exercícios \n 1 - Quais números são pares? \n 2 - Idades \n 3 - Estoque \n 4 - Notas de alunos\n Digite uma opção: "))
    os.system('cls')
    match menuA:
#Programa para saber qantos números ímpares e pares foram inseridosno vetor        
        case 1:           
            for count in range (5):
                 num1.append(int(input("Digite um número: "))) 
                 if (num1[count]%2) == 0:
                        par = par + 1
                 else:
                        impar = impar + 1
            print("Você digitou %d números pares e %d de números ímpares" % (par, impar))        
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls') 
#Programa para saber qual foi a idade minima e maxima e a média inserida no vetor            
        case 2:
            idade = []
            for count in range (5):
                idade.append(int(input("Digite sua idade: ")))
            print("Esta foi a menor idade digitada: %d"% min(idade))
            print("Esta foi a maior idade digitada: %d"% max(idade))
            mean = statistics.mean(idade)
            print("Esta foi a menor idade digitada: %d"% mean)
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls') 
#Programa para saber o preço e se tem no estoque o produto dentro das escolhas. As escolhas e sues dados estão inseridas em um dicionário          
        case 3:
            produtos = {"Pizza": [25, True], "Farofa": [8,True], "Morango": [7.50, False], "Feijão": [8.99,False] }
            pesquisa = input("Qual produto deseja comprar?\n Pizza\n Farofa\n Morango\n Feijão\n Inisra o nome do produto: ")
            if produtos[pesquisa][1] == False:
                print("Produto sem estoque")
            else:
                print(pesquisa, "tem o valor de: R$%d" % produtos[pesquisa][0]) 
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls') 
#Programa para inserir o nome do aluno para ser mostrado suas notas que serão geradas aleatoriamente                
        case 4:
            alunos = {"Roberto": [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)], "Marcelo": [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)], "Pâmela": [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)], "Júlia": [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)], "Valentina": [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)] }
            pesquisa = input("Qual aluno deseja ver a nota?\n Roberto\n Marcelo\n Pâmela\n Júlia\n Valentina\n Inisra o nome do produto: ")
            print(pesquisa, "tem as seguintes notas:\n Matemática: %s\n Português: %s\n Biologia: %s\n Inglês: %s\n História: %s\n " % (alunos[pesquisa][0], alunos[pesquisa][1], alunos[pesquisa][2], alunos[pesquisa][3], alunos[pesquisa][4])) 
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls') 