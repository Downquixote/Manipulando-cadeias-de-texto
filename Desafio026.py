# Faça um programa que leia uma frase pelo teclado e mostre: 
# 1 - Quantas vezes aparece a letra "A"
# 2 - Em que posição ela aparece a primeira vez
# 3- Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantidade de "A" que sua frase possui: ', frase.count('A', 0))

print('O primeiro "A" da sua frase aparece na posição: ', frase.find('A')+1)

print('O último "A" da sua frase aparece na posição: ', frase.rfind('A')+1)