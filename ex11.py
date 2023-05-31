"""
 Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe a média de preço de custo e do preço de venda.
"""

soma_custo = 0
soma_venda = 0


for i in range(1, 41):
    print(f"Produto {i}")
    preco_custo = float(input("Preço de custo: "))
    preco_venda = float(input("Preço de venda: "))

    
    if preco_venda > preco_custo:
        resultado = "Lucro"
    elif preco_venda < preco_custo:
        resultado = "Prejuízo"
    else:
        resultado = "Empate"

    
    soma_custo += preco_custo
    soma_venda += preco_venda


    print(f"Resultado: {resultado}")
    print("")


media_custo = soma_custo / 40
media_venda = soma_venda / 40


print(f"Média de preço de custo: R$ {media_custo:.2f}")
print(f"Média de preço de venda: R$ {media_venda:.2f}")


