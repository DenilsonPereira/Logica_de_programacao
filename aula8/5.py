#Pede dois números (base e expoente) calcule o primeiro número elevado ao segundo número
base=int(input("Digite uma base: "))
expoente=int(input("Digite um expoente: "))
potencia = base

while(expoente != 1):
    potencia = potencia*base
    expoente = expoente-1
print(potencia)