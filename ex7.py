"""
Ler 80 números e ao final informar quantos número(s) está ou estão no intervalo entre 10 (inclusive) e 150 (inclusive) 
"""
import random
contador = 0

for i in range (0,81):
    a = random.randint(0,1000)
    print(a)
    if a>= 10 and a<=150:
        contador +=1
print(f'Existem {contador} números entre 10 e 150! ')

