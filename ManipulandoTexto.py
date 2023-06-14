# Fatiamento
frase = 'Conhecimento em Python'
print(frase[0:7])

# Análise
print(len(frase))

print(frase.count('o'))
print(frase.count('o', 7, 13))

print(frase.find('on'))

print('Python' in frase)

# Transformação
print(frase.replace('Python','Windows'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

frase2 = '   Programação Back End    '
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

# Divisão
print(frase2.split())

# Junção
print('-'.join(frase))