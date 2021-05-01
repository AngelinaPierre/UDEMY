"""
PEP8 - PYTHON ENHANCEMENT PROPOSAL

São propostas de melhorias para a linguagem python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever codigos python de forma pythonica (visualmente agradavel).

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class calculadora_cientifica:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funções ou variaveis;

def soma():
    pass

def soma_dois():
    pass

numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para identação!***SUPER IMPORTANTE*** (não utilize tab, pode ter configurações diferentes)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- metodo dentro de uma classe devem ser separados com uma unica linha em branco/

[5] - imports
- Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys,os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

[6] - Espaços em expressões e instruções

# Não Faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro:2})

# Não Faça:

algo (1)

# Faça:

algo(1)

# Não Faça:

dict ['chave'] = list [indice]

# Faça:

dict['chave']= list[indice]

# Não Faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha


"""
import this
