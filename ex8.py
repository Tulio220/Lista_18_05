"""
Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.
"""

import random

for i in range (0,76):
    a = random.randint(0,100)
    if a< 18:
        print(f'Tendo {a} anos é MENOR DE IDADE! ')
    else:
        print(f'Tendo {a} anos é MAIOR DE IDADE! ')