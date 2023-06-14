# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas minúsculas
# 3 - Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: ')).strip()
print('Nome inteiro em maiúsculo: ', nome.upper()) 

print('Nome inteiro em minúsculo: ', nome.lower())

espaco = nome.replace(" ", "")
qtd = len(espaco)
print('Quantidade de caracteres: ', qtd)

primeiro = nome.split()[0]
nome1 = len(primeiro)
print('Quantidade de letras no primeiro nome: ', nome1)