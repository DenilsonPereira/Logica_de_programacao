#Implemente uma função recursiva que, dados dois números inteiros x e n, calcula o valor de x^n.
def elevado(x,n):
    if n == 0: return 1
    else: return x * elevado(x,n - 1)
print(elevado(3,4))