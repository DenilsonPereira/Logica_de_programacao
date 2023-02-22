Algoritmo "Idade em dias"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Lucas Sampaio
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Denilson da Silva Pereira
// Data atual  : 17/02/2023
Var
// Seção de Declarações das variáveis 
   anos, meses, dias, idade: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
  escreval("Informe a idade em anos, meses e dias: ex.:(15,10,30)")
  leia(anos, meses, dias)
  idade<-(anos*365)+(meses*30)+dias
  escreva("Idade em dias é:", idade)

Fimalgoritmo