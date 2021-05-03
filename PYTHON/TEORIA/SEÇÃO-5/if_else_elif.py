"""
Estruturas condicionais
if (se), else(se não), elif (else if)

- A partir que utilizamos estruturas condicionais no nosso progama deixamos ele mais "inteligente"
- Expandimos mais ele, onde damos caminhos diferentes para resolver problemas.

- Na estrutura If do python não existe parenteses (redundancia), quando vamos iniciar um novo
bloco no python colocamos os dois pontos(:)
    - O python espera que o proximo bloco inicie 4 ESPAÇOS depois do bloco que esta finalizando.
        - Não colocar mostra erro.
"""

idade = 26

# o que diferencia python de outras linguagens
"""
# Linguagem C - Estrutura condicional if, else em C
    if(idade<18){
        printf("Menor de Idade");
    }else{
        printf("Maior de idade");
    }
"""
"""
# Linguagem java - Estrutura condicional if , elseem JAVA
    if(idade<18){
        System.out.println("Menor de Idade");
    }else{
        System.out.println("Maior de idade");
    }
"""


# if idade < 18:
#     print('Menor de idade')
#     print(idade)
# else:   #espera 2 pontos (:) e a indentação (4 espaços) - finalizar com uma nova linha.
#     print('Maior de idade')


#elif em C seria:
"""
    if(idade<18){
        printf("Menor de idade!");
    }else if(idade == 18){
        printf("Tem 18 anos");
    }else{
        printf("É menor de idade");
    }
"""
#elif em JAVA seria:
"""
    if (idade < 18){
        System.out.println("Menor de idade!");
    } else if (idade == 18){
        System.out.println("Tem 18 anos");
    } else {
        System.out.println("É menor de idade");
    }
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')

# não estruturado - bad
if idade < 18:
    print('Menor de idade')

if idade == 18:
    print('Tem 18 anos')

if idade == 26:
    print('Tem 26 anos')

if idade > 18:
    print('Maior de idade')