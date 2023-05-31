"""
Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número
"""

pergunta = int(input('Quantas vezes quer jogar? '))

for i in range(pergunta):
    numero = int(input("Digite seu número: "))
    if numero <0:
        print("Negativo!")
    if numero == 0:
        print("Zero!")
    if numero >0:
        print("Positivo!")
