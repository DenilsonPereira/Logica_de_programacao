'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

valorHora = float(input("Qual o valor da hora? "))
quantHorasTrab = float(input("Quantas horas foram trabalhadas esse mês: "))

salarioBruto = valorHora*quantHorasTrab
impostoRenda = salarioBruto*0.11
inss = salarioBruto*0.08
sindicato = salarioBruto*0.05
salarioLiquido = salarioBruto-impostoRenda-inss-sindicato

print(f"Salário Bruto: R${salarioBruto:.2f}")
print(f"IR(11%): R${impostoRenda:.2f}")
print(f"INSS(8%): R${inss:.2f}")
print(f"Sindicato(5%): R${sindicato:.2f}")
print(f"Salário Líquido: R${salarioLiquido:.2f}")