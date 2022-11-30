value = 1
total = 0
quant = 0
import os 

while value >-1:
    value=int(input("Digite um número \n")) 
    quant = quant + 1
    os.system('cls')
    total = (total + value) / quant
    int(total)
    print("A média é %s! " %total) 