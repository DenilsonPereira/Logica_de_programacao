#Crie uma função recursiva para dado uma lista de inteiros e o seu número de elementos, inverta a posição dos seus elementos.
def atsil(lista):
    if len(lista) <= 1: return lista
    else: return lista[-1:] + atsil(lista[:-1])

print(atsil([18,6,250]))
