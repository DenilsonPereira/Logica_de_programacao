Algoritmo "Numero maior e menor"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Lucas Sampaio
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Denilson da Silva
// Data atual  : 10/02/2023
Var
// Seção de Declarações das variáveis 
   num, cont, maior, menor: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
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
   escreval("O número maior é: ", maior, " e o número menor é: ", menor)

Fimalgoritmo