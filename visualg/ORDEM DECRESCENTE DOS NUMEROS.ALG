Algoritmo "Ordem decrescente dos numeros"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Lucas Sampaio
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Denilson da Silva Pereira
// Data atual  : 10/02/2023
Var
// Se��o de Declara��es das vari�veis
   n1, n2, n3: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
   n1<-0
   n2<-0
   n3<-0
   leia(n1)
   leia(n2)
   leia(n3)
   se ((n1>n2)e(n1>n3)e(n2>n3)) entao
      escreval(n1,n2,n3)
   fimse
   se ((n1>n3)e(n1>n2)e(n3>n2)) entao
      escreval(n1, n3,n2)
   fimse
   se ((n2>n3)e(n2>n1)e(n3>n1)) entao
      escreval(n2, n3, n1)
   fimse
   se ((n2>n1)e(n2>n3) e (n1>n3)) entao
      escreval(n2, n1, n3)
   fimse
   se((n3>n1)e(n3>n2)e(n1>n2)) entao
      escreval(n3, n1, n2)
   fimse
   se ((n3>n1)e(n3>n2)e(n2>n1)) entao
      escreval(n3,n2,n1)
   fimse



Fimalgoritmo