#Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.
def ocorre(k,n):
    if k[0]<9: return k
    else: return k[0]==n + ocorre(k[-1],n)
print(ocorre('762021192', '2'))