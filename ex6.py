"""
Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
A atribuição de conceitos obedece a tabela abaixo:

Média de Aproveitamento | Conceito
MA >= 9,0               | A
7,5 <= MA < 9,0         | B
6,0 <= MA < 7,5         | C
4,0 <= MA < 6,0         | D
MA < 4,0                | E

O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A, B ou C e REPROVADO se o conceito for D ou E. Pergunte se o usuário deseja digitar as notas de outro aluno S para sim e N para não
 
"""

p = input('Deseja cadastrar um aluno? \n')

while p.upper()!="SIM" and p.upper()!="NÃO" and p.upper()!="NAO":
    print('Resposta inválida, digite novamente!')
    p = input('Deseja cadastrar um aluno? \n')

while p.upper()!="NÃO" and p.upper()!="NAO":
    identificacao = int(input('Digite seu número de identificação: '))

    n1 = int(input('Digite sua primeira nota: '))
    while n1 < 0:
        print('Nota inválida, digite novamente!')
        n1 = int(input('Digite sua primeira nota: '))

    n2 = int(input('Digite sua segunda nota: '))
    while n2 < 0:
        print('Nota inválida, digite novamente!')
        n2 = int(input('Digite sua segunda nota: '))

    n3 = int(input('Digite sua terceira nota: '))
    while n3 < 0:
        print('Nota inválida, digite novamente!')
        n3 = int(input('Digite sua terceira nota: '))

    me = int(input('Digite a nota dos exercícios: '))
    while me < 0:
        print('Nota inválida, digite novamente!')
        me = int(input('Digite a nota dos exercícios: '))

    ma = (n1 + n2 * 2 + n3 * me)/7  
    if (ma>9.0):
        print(f'Parabéns {identificacao}, voce foi APROVADO! Sua média foi {ma} e você ficou com nota A! \n Suas notas foram: Nota 1:{n1},Nota 2:{n2}, Nota 3:{n3},Nota dos exercícios:{me}')

    if (ma>= 7.5 and ma <9.0):
        print(f'Parabéns {identificacao} voce foi APROVADO! Sua média foi {ma} e você ficou com nota A! \n Suas notas foram: Nota 1:{n1},Nota 2:{n2}, Nota 3:{n3},Nota dos exercícios:{me}')

    if (ma>= 6.0 and ma <7.5):
        print(f'Parabéns {identificacao}, voce foi APROVADO! Sua média foi {ma} e você ficou com nota A! \n Suas notas foram: Nota 1:{n1},Nota 2:{n2}, Nota 3:{n3},Nota dos exercícios:{me}')

    if (ma>= 4.0 and ma <6.0):
        print(f'Parabéns {identificacao}, voce foi APROVADO! Sua média foi {ma} e você ficou com nota A! \n Suas notas foram: Nota 1:{n1},Nota 2:{n2}, Nota 3:{n3},Nota dos exercícios:{me}')

    if (ma  <4.0):
        print(f'Parabéns {identificacao}, voce foi APROVADO! Sua média foi {ma} e você ficou com nota A! \n Suas notas foram: Nota 1:{n1},Nota 2:{n2}, Nota 3:{n3},Nota dos exercícios:{me}')

    p = input('Deseja cadastrar um aluno? \n')

    while p.upper()!="SIM" and p.upper()!="NÃO" and p.upper()!="NAO":
        print('Resposta inválida, digite novamente!')
        p = input('Deseja cadastrar um aluno? \n')


