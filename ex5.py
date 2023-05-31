"""
Faça um programa que calcule e mostre a média aritmétca de N notas. N equivale ao total de avaliações.
"""
numero = int(input('Digite a quantidade de notas que serão inseridas: '))

while numero < 0:
    print('Número Inválido')
    numero = int(input('Digite a quantidade de notas que serão inseridas: '))

media = 0
for i in range(numero):
    notas = float(input("Digite sua nota: "))
    qtd = notas + media 
    media = qtd 
soma = media / numero 
print(soma)


    

    

print(f'Sua media aritmética foi: {soma}')

"""a = 0
b = 1
#inicio
print(a, end=", ")
print(b, end=", ")
"geração 2"
c = a + b
print(c, end=", ")
#atualizar
a = b
b = c
#geração 3
c = a+b
print(c, end=", ")
"""