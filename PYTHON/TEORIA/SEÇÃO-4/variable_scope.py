"""
Escopo de variaveis

Escopo = limitação de algo
/_______________escopo_________________/

quando falamos de variáveis temos dois casos de escopo:
1 - Escopo das variaveis globais
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende todo o progama.
2 - Escopo das variaveis locais
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

para declarar variaveis em python fazemos:
nome_da_variavel = valor_da_variavel

python é uma linguagemd e tipagem dinamica. isso significa que
ao declararmos uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

"""
numero = 42 # exemplo de variavel global
print(numero)
print(type(numero))

numero = 'geek'
print(numero)
print(type(numero))

#exemplo de variavel local

numero = 42

if numero > 10:
    novo = numero + 10 # a variavel novo esta declarada localmente dentro do bloco if
    print(novo)

print(novo)