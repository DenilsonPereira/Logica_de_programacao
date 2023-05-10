#Faça um programa para imprimir de acordo com a imagem a baixo para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def triangulo(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=' ')
        print()
    n=' '
    return n
print(triangulo(6))