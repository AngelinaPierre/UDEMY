"""
BOOLEAN

Algebra Booleana, criada por George Boole

2 cosntantes, Verdadeiro ou Falso

true -> Verdadeiro
False -> Falso

OBS: Sempre com a inicual minuscula

Errado:
true, false

Certo:
True, False

"""

# estamos fazendo um sistema para verificar se o usuario esta ativo nele.

ativo = True

print(ativo)

"""
Operações basicas
"""

# negação(not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso, o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# ou (or)
"""
É uma operação binaria, ou seja, depende de dois valores. Ou um ou outro devem ser verdadeiro.
# console -> True or True  = true
# console -> True or False = True
# console -> False or True = True
# console -> False or False = False
"""

print(ativo or logado)

# E(and):
"""
Tambem é uma operação binaria, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
