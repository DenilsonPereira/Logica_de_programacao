Algoritmo "media aluno"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Lucas Sampaio
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Denilson da Silva Pereira
// Data atual  : 10/02/2023
Var
// Seção de Declarações das variáveis 
   nota1, nota2, media: real;

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   leia(nota1)
   leia(nota2)
   media<-(nota1+nota2)/2
   
   se (media>=7) e (media<=9) entao
      escreva("Aprovado")
   senao
        se (media=10) entao
           escreva("Aprovado com Distinção")
        senao
             escreva ("Reprovado")
        fimse
   fimse

Fimalgoritmo