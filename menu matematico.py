menuB = 1
import os
import random
while menuB == 1:
    menuA = int(input("Qual operação deseja fazer?\n 1 - Multiplicação\n 2 - Soma\n 3 - Subtração\n 4 - Divisão\n 5 - Fatorial\n 6 - Porcentagem ímpares\n 7 - Números entre 100 e 200\n 8 - Dados\n 9 - Bínario para decima\n"))
    os.system('cls')
    match menuA:
        case 1:
            tabuada = int(input("Tabuada de um número de 1 a 10: "))
            if tabuada < 1 or tabuada > 10:
                print("Número inválido\n")
                menuB = 1
                os.system('cls')
            else:
                for count in range(10):
                    print("%d X %d = %d" % (tabuada, count+1, tabuada*(count + 1)))
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))   
            os.system('cls')     
        case 2:   
            tabuada = int(input("Tabuada de um número de 1 a 10: "))
            if tabuada < 1 or tabuada > 10:
                print("Número inválido\n")
                menuB = 1
                os.system('cls')
            else:
                for count in range(10):
                    print("%d + %d = %d" % (tabuada, count+1, tabuada+(count + 1)))
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))   
            os.system('cls')
        case 3:    
            tabuada = int(input("Tabuada de um número de 1 a 10: "))
            if tabuada < 1 or tabuada > 10:
                print("Número inválido\n")
                menuB = 1
                os.system('cls')
            else:
                for count in range(10):
                    print("%d - %d = %d" % (tabuada, count+1, tabuada-(count + 1)))
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))
            os.system('cls')
        case 4:
            tabuada = int(input("Tabuada de um número de 1 a 10: "))
            if tabuada < 1 or tabuada > 10:
                print("Número inválido\n")
                menuB = 1
                os.system('cls')
            else:
                for count in range(10):
                    print("%d : %d = %d" % (tabuada, count+1, tabuada/(count + 1)))
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n")) 
            os.system('cls')
        case 5:
            fatorial = int(input("Digite um número de 1 a 10: "))
            result = 1
            for count in range (1,fatorial+ 1):
                result *= count
                print(result)
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls')    
        case 6:
            par = 0
            impar = 0
            result = 0    
            for count in range(10):
                number = int(input("Digite o %dº número " % (count+1))) 
                if (number%2) == 0:
                    par = par + 1
                else:
                    impar = impar + 1
                result = ((impar/100)*(impar+par)) *100 
                print("A porcentagem de números ímpares inseridos foi de: %d porcento" % result)  
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls')    
        case 7:
            enterNum = 0
            for count in range(10):
                num = int(input("Digite o %d número" % (count+1)))
                if num >= 100 and num <= 200:
                    enterNum = enterNum + 1
                print("São %d número(s) dentro do intervalo" % enterNum ) 
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls')  
        case 8:
            dice = 0
            for count in range(100):
                dice = random.randint(0,6)
                print("O %dº resultado é: %d" % (count+1, dice))
            menuB = int(input("Deseja voltar para o menu?\n 1 -- Sim\n 2 -- Não\n"))  
            os.system('cls')
        case 9:
            binario = int(input("Digite seu número em binário: "))
            n = len(str(binario))
            valorDigitado = binario
            decimal = 0
            i = 0
            while n >= 0:
                resto = binario % 10
                decimal =  decimal + (resto * (2**i))
                n = n - 1
                i = i + 1
                binario = binario // 10
            print("O número binário digitado %d na base decimal, vale: %d" % (valorDigitado, decimal))    


