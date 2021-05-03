"""
ESTRUTURAS LÓGICAS
AND (e), OR (ou), NOT (não), IS (é)

OPERADORES UNÁRIOS:
    - not
    -
OPERADORES BINÁRIOS:
    - and
    - or
    - is
REGRAS DE FUNCIONAMENTO
- Para o AND, ambos os valores precisam ser TRUE
- Para o OR, um ou outro valor precisa ser TRUE
- Para o NOT, o valor do BOOLEANO é invertido, True = False | False  = True
- Para o IS, o valor é comparado com um segundo.


"""

ativo = True
logado = False

# if ativo and logado:
#     print('Welcome User!')
# else:
#     print('You need to activate your account, please check your email!')


# if ativo or logado:
#     print('Welcome User!')
# else:
#     print('You need to activate your account, please check your email!')

# se não estiver ativo
# if not ativo:
#     print('You need to activate your account, please check your email!')
# else:
#     print('Welcome User!')
#
# print(not False)

# if ativo is False:
#     print('You need to activate your account, please check your email!')
# else:
#      print('Welcome User!')

# jeito pythonico eh com o if not

# if ativo:
#     print('Welcome user!')
# else:
#     print('You need to activate your account, please check your email!')

# #ativo é falso?
# print(ativo is False)

nome = 'Angelina'
#nome esta em maisculo?
print(nome.isupper())
#a inical esta em maisculo?
print(nome.istitle())

print(nome.title().istitle())

print(1 is 1)

