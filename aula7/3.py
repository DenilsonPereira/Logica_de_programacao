valorHora = float(input("Informe seu valor hora: "))
quantHora = float(input("Informe quantas horas: "))
salarioBruto = valorHora*quantHora
print("Salário Bruto:"," "*10,f"R${salarioBruto}")
if salarioBruto<=900:
    ir = 0
    print("(-) IR (Isento):"," "*8,f"R${ir}")
elif salarioBruto>900 and salarioBruto<=1500:
    ir = (salarioBruto*5)/100
    print("(-) IR (5%):"," "*12,f"R${ir}")
elif salarioBruto>1500 and salarioBruto<=2500:
    ir = (salarioBruto*10)/100
    print("(-) IR (10%):"," "*11,f"R${ir}")
elif salarioBruto>2500:
    ir = (salarioBruto*20)/100
    print("(-) IR (20%):"," "*11,f"R${ir}")
sindicato = (salarioBruto*3)/100
print("(-) Sindicato (3%):"," "*5,f"R${sindicato}")
fgts = (salarioBruto*11)/100
print("FGTS (11%):"," "*13,f"R${fgts}")
totalDesconto = ir+sindicato
print("Total de descontos:"," "*5,f"R${totalDesconto}")
salarioLiquido = salarioBruto-ir-sindicato
print("Salário Liquido:"," "*8,f"R${salarioLiquido}")