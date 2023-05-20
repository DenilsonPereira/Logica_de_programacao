#Escreva uma função que recebe como entrada um número n e imprime todas as potências de 2 menores ou iguais a n.
def potencias(n):
    p=0
    r=1
    while r<=n:
        print(r)
        p+=1
        r=2**p
    return ''
print(potencias(20))