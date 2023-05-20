#Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente.
n=int(input("Informe: "))
def naturais(n):
    l=[]
    for i in range(n+1):
        l.append(i)
    p=l[::-1]
    for j in range(n+1):
        print(p[j], end=" ")
naturais(n)