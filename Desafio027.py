# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza
nome = str(input('Qual seu nome? ')).strip()
first = nome.split()
print('Primeiro nome: {}'.format(first[0]))
print('Último nome: {}'.format(first[len(first)-1]))