value = 1
maior = 0
menor = 0
import os 

while value != 0 and value > 0:
    value=int(input("Digite um número \n")) 
    os.system('cls')
    if value > maior:
        maior = value
    elif value < menor: 
        menor = value
    print("O maior número é %s! " %maior)       