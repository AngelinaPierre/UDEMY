"""
Recebendo dados do usuario

Input() -> entrada _> todo dado recebido via input é do tipo string

    Em python, string é tudo o que estiver entrE:
        - ASPAS SIMPLES
        - ASPAS DUPLAS
        - ASPAS SIMPLES TRIPLAS
        - ASPAS DUPLAS TRIPLAS
    EXEMPLOS:
    - ASPAS SIMPLES -> 'ANGELINA JOLIE'
    - ASPAS DUPLAS -> "ANGELINA jOLIE"
    - ASPAS SIMPLES TRIPLAS -> '''aNGELINA jOLIE'''
    - ASPAS DUPLAS TRIPLAS ->  BUGA POIS ESTA DENTRO DE UM COMENTARIO(PROVAVELEMNTE SE ANULAM)
print() -> imprime na tela

() -> quando temos uma variavel, não precisamos colocar o parenteses, se for mais de uma eh necessario.

"""
#entrada de dados
#print("Qual o seu nome?")
#nome = input()

nome = input('Qual o seu nome?')

# Exemplo de print 'antigo' 2.X
# print('seja bem-vindo(a) %s' % nome)

#Exemplo de print moderno
# print('Seja bem-vindo(a) {0}'.format(nome))

#Exemplo de print atual
print(f'Seja bem-vindo(a) {nome}')

#print('Qual a sua idade?')
#idade = input()

#idade = input('Qual sua idade?')

#com casting
idade = int(input('Qual sua idade?'))

#processamento

#saida de dados

# Exemplo de print 'antigo' 2.X
#print('A %s tem %s anos' % (nome, idade))

#Exemplo de print moderno
#print('A {0} tem {1} anos'.format(nome,idade))

#Exemplo de print atual
print(f'A {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a "conversão" de um tipo de dado para outro
"""
# print(f'A {nome} nasceu em {2018 - int(idade)}')

#casting feito no input
print(f'A {nome} nasceu em {2018 - idade}')