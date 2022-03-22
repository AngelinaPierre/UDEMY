# ==== [SEÇÃO 2 - PREPARANDO O AMBIENTE ] ====

&nbsp;

---

---

## [Aula 5] - INSTALAÇÃO E CONFIGURAÇÃO NO WINDOWS

&nbsp;


Sempre utilize a ultima versão do **SISTEMA OPERACIONAL**
Precisamos instalar o **JDK**, que é a biblioteca de *Execução* e *Desenvolvimento* do **JAVA**.
Precisamos instalar o **ECLIPSE**, que será nossa biblioteca de desenvolvimento JAVA. O proprio *eclipse* precisa do java para funcionar.



    1 - Primeiro instalar o JDK. Ver local onde a instalação esta sendo feita.
    2 - Ver se adicionou os binario no sistema.
    3 - Verificar se o comando java é reconhecido.

~~~
java --version
~~~


    1 - Apos a instalação do ECLIPSE, vamos fazer um teste criando um arquivo [.java].
    -> O nome do novo PROJETO JAVA será [GeekJava], o projeto será criado dentro do WORKSPACE que configuramos e será tambem mostrado a versão do JAVA que esta sendo utilizado.
    -> Podemos desmarcar a caixa ded criação do MODULO DE INFORMAÇÃO para não criar esse modulo.
    -> Note que ao criarmos nosso projeto, temos 2 DIRETORIOS CRIADOS AUTOMATICAMENTE.
        - [JRE SYSTEM LIBRARY] - bibliotedcapadrão do java
        - [SRC] - SOURCE CODE, onde iremos escrever o codigo fonte.
    -> Vamos criar um NEW PACKAGE dando o nome de GEEK, para fazermos um teste. Esse packge so serve apra organizar codigo, teremos uma aula especifica sobre ele. 
    -> Dentro do package que criamos vamos criar uma NOVA CLASSE e chama-la de PROGAMA 1, marcandoa  caixa de PUBLIC STATIC VOID MAIN(STRING[] ARG).   
        - Sempre que criarmos uma classe java o nome dessa classe inicia com letra maiuscula, sem espaços, sem acentos ou caracteres especiaias.
        - Vamos marcar essa caixa para que a IDE crie essa função para ser o nosso progama java.
    ->  Apos criarmos nossa classe, vamos ter esse codigo incial abaixo.

~~~java
package geek;

public class Progama1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

~~~

    2 - Vamos colocar um ''PRINT'' para vermos se nossa IDE esta rodando nossos progamas.
    -> Usar ponto e virgula no final [;], e salvar o progama antes de rodar.
~~~java
package geek;

public class Progama1 {

	public static void main(String[] args) {
		System.out.println("Geek University");

	}

}
~~~


&nbsp;

---

---

## [Aula 6] - INSTALAÇÃO E CONFIGURAÇÃO NO LINUX

&nbsp;

&nbsp;

---

---

## [Aula 7] - INSTALAÇÃO E CONFIGURAÇÃO NO MACOS

&nbsp;

&nbsp;

---

---

## [Aula 8] - RECAPITULANDO

&nbsp;


&nbsp;

&nbsp;


# ==== [SEÇÃO 3 - INTRODUÇÃO À LINGUAGEM JAVA ] ====



&nbsp;

---

---

## [Aula 9] - O QUE VAMOS APRENDER NESTA SEÇÃO

&nbsp;



Vamos nesta seção sobre o que é o JAVA, variaveis, compiladores, função main(). Ou seja, essa seção fará voce entender o que é JAVA e tudo o que envolve essa linguagem de progamação.





&nbsp;

---

---

## [Aula 10] - A LINGUAGEM JAVA, JRE, JDK E ECOSSISTEMA JAVA

&nbsp;


~~~text
                            [JAVA]
        [JVM]       [JDK]       [JRE]       [LINGUAGEM JAVA]
~~~



&nbsp;

---

---

## [Aula 11] - VARIAVEIS

&nbsp;