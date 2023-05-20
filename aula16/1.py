#Faça um programa em que dada uma lista de números inteiros,encontre o segundo menor e o segundo maior valor sem ordenar a lista:
n = [5,9,2,1,3]
print(n)
for i in n:
    maior = n.index(max(n))
del n[maior]
for i in n:
    menor = n.index(min(n))
del n[menor]
print(max(n),min(n))