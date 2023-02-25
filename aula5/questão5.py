#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número em decimal: "))

#a. o produto do dobro do primeiro com metade do segundo
prod = (num1*2)*(num2/2)
print(prod)
#b. a soma do triplo do primeiro com o terceiro.
tri = (3*num1)+num3
print(tri)
#c. o terceiro elevado ao cubo.
elevado = num3**3
print(elevado)