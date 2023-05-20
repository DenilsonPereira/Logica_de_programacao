#Escreva uma função para imprimir o valor absoluto de um número. (obs: utilize apenas operações aritméticas).
n=int(input("Informe: "))
def absoluto(n):
    if n<0:
        n= -n
        print(n)
    else:
        print(n)
absoluto(n)