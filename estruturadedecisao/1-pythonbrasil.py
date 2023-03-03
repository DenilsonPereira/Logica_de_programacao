#Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if n1>n2:
    print(n1)
elif n2>n1:
    print(n2)
else:
    print("{0} é igual a {1}".format(n1,n2))