Algoritmo "media aluno"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Lucas Sampaio
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Denilson da Silva Pereira
// Data atual  : 10/02/2023
Var
// Se��o de Declara��es das vari�veis 
   nota1, nota2, media: real;

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   leia(nota1)
   leia(nota2)
   media<-(nota1+nota2)/2
   
   se (media>=7) e (media<=9) entao
      escreva("Aprovado")
   senao
        se (media=10) entao
           escreva("Aprovado com Distin��o")
        senao
             escreva ("Reprovado")
        fimse
   fimse

Fimalgoritmo