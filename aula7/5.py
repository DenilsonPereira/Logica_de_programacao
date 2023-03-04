print("É um triângulo?")
l1 = int(input("Informe um número: "))
l2 = int(input("Informe outro número: "))
l3 = int(input("Informe mais um número: "))

if (l1+l2>l3) and (l1+l3>l2) and (l2+l3>l1):
    print("É um triângulo")
    if l1==l2==l3:
        print("Triângulo Equilátero")
    elif (l1==l2) or (l2==l3) or (l1==l3):
        print("Triangulo Isósceles")
    elif l1!=l2!=l3:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")
