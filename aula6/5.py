salario = float(input("Informe seu salário: "))
codigo = int(input("Informe o código do seu cargo: "))

if(codigo==310):
    aumento = salario+((salario*5)/100)
    print("Seu novo salário é R$ {}".format(aumento))
elif (codigo==456):
    aumento = salario+((salario*7.5)/100)
    print("Seu novo salário é R$ {}".format(aumento))
elif (codigo==885):
    aumento = salario+((salario*10)/100)
    print("Seu novo salário é R$ {}".format(aumento))
else:
    aumento = salario+((salario*15)/100)
    print("Seu novo salário é R$ {}".format(aumento))