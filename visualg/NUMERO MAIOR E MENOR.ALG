Algoritmo "Numero maior e menor"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Lucas Sampaio
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Denilson da Silva
// Data atual  : 10/02/2023
Var
// Se��o de Declara��es das vari�veis 
   num, cont, maior, menor: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   cont<-0
   enquanto cont<3 faca
       leia(num)
       
       se cont=0 entao
          maior<-num
          menor<-num
       fimse
         se num>maior entao
            maior<- num
         fimse
         se num<menor entao
            menor<-num
         fimse
         
       cont<-cont+1
   fimenquanto
   escreval("O n�mero maior �: ", maior, " e o n�mero menor �: ", menor)

Fimalgoritmo