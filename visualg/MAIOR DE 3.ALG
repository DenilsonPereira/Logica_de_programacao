Algoritmo "Maior de 3"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Lucas Sampaio
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Denilson da Silva Pereira
// Data atual  : 17/02/2023
Var
// Se��o de Declara��es das vari�veis 
    n1,n2,n3: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
    leia(n1,n2,n3)
    se ((n1>n2) e (n1>n3)) entao
       escreva(n1)
    senao
         se ((n2>n1) e (n2>n3)) entao
            escreva(n2)
         senao
              se ((n3>n1) e (n3>n2)) entao
                 escreva(n3)
              fimse
         fimse
    fimse


Fimalgoritmo