n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um terceiro número: "))
aux = 0

if (n1 > n2):
    aux = n2
    n2 = n1
    n1 = aux
if (n1 > n3):
    aux = n3
    n3 = n1
    n1 = aux
if (n2 > n3):
    aux = n3
    n3 = n2
    n2 = aux
print(n1)
print(n2)
print(n3)
    