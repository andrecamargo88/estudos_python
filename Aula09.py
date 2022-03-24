frase = 'Curso em Video Python'
# ...... 012345678901234567890.....

# Fatiamento:
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[15:])
print(frase[9::3])

# Analise:
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))   # resp. '-1' sig. que nao tem a palavra.
print('Curso' in frase)

frase2 = '   Curso em Video Python  .  '
#.........012345678901234567890123456789.......

print(len(frase2))

# transformação
print(frase2.replace('Python', 'Android'))
print(frase2.strip())   # corta espaços vazions no inicio e no fim
print(frase2.rstrip())  # corta espaços vazions a direita
print(frase.upper())    # Coloca tudo em maiusculo
print(frase.lower())    # Coloca tudo em minusculo
print(frase.capitalize())  # Coloca todas as letras em minusculo e deixa apenas a primeira letra em maiusculo.
print(frase.title())    # Coloca todas as primeiras letras em maiusculo.

# Divisão
frase.split()     # Separa todas as palavras e cria um novo index para cada palavra.
print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2])
print(dividido[2][3])

# Junção
' '.join(frase)   # Junta as palavras unindo em uma unica indexação.