"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as infornações
"""
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while senha == nome:
    print("Senha Inválida!")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
