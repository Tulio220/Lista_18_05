"""
Uma concessionária de veículos está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar total de carros com ano até 2000 e total geral.
"""
total_carros_ate_2000 = 0
total_geral = 0

while True:
    ano = int(input("Digite o ano do veículo (0 para sair): "))
    
    if ano == 0:
        break
    
    valor = float(input("Digite o valor do veículo: "))
    
    if ano <= 2000:
        desconto = valor * 0.12
        total_carros_ate_2000 += 1
    else:
        desconto = valor * 0.07
    
    valor_pago = valor - desconto
    total_geral += 1
    print("="*30)
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a ser pago: R${valor_pago:.2f}")
    print()
    
print(f"Total de carros até 2000: {total_carros_ate_2000}")
print(f"Total geral:{total_geral}")
