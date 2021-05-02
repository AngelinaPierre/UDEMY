"""

STRING TYPE

Em python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'uma string, '234', 'a', 'true', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "true", "42.3"
- Estiver entre aspas simples triplas ->'''uma string''', '''234''', '''a''', '''true''', '''42.3'''
- Estiver entre aspas duplas triplas ->

# mais comum colocar aspas simples
nome = '''Angelina Pierre'''
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

# \n serve para pular uma linha
nome = 'Angelina \nPierre'
print(nome)
print(type(nome))

# a utilização do caractere de escape (\) permite imprimir a aspas dupla
nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

nome = 'Angelina Jolie'
print(nome.upper())

nome = 'Angelina Jolie'
print(nome.lower())

# pega cada uma das palavras separadas por espaço e coloca em uma lista
nome = 'Angelina Jolie'
print(nome.split())
            [0]          [1]
console -> ['Angelina', 'Pierre']
-> Conseguimos trabalhar de forma indexada
->         [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13 ]
console -> ['A','n','g','e','l','i','n','a',' ','J','o','l','i','e']
Sempre que falamos em listas a primeira posição eh o 0 e a ultima eh n-1

# Essa operação eh chamada de SLICE DE STRING
print(nome[0:4])  # do 0 ate o 3

print(nome[5:14])

print(nome.split()[0])
print(nome.split()[1])
"""

# pega cada uma das palavras separadas por espaço e coloca em uma lista
nome = 'Angelina Jolie'

# invertendo a string
print(nome[13], nome[12])

"""
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta.
"""
print(nome[::-1])

# trocando letras nas strings
print(nome.replace('g', 'p'))
