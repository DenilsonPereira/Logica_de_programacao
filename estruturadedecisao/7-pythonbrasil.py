#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

if n1>n2 and n1>n3:
    print("Maior: ",n1)
elif n2>n1 and n2>n3:
    print("Maior: ",n2)
elif n3>n1 and n3>n2:
    print("Maior: ",n3)

if n1<n2 and n1<n3:
    print("Menor: ",n1)
elif n2<n1 and n2<n3:
    print("Menor: ",n2)
elif n3<n1 and n3<n2:
    print("Menor: ",n3)