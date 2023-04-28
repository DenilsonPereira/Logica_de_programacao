'''Dada uma lista de números, escreva um programa Python para criar uma lista de tuplas tendo o primeiro elemento como o número e o segundo elemento como o cubo do número.'''
lista=[9,5,6,20]
lista2=[]
for i in range(len(lista)):
    tupla=(lista[i], lista[i]**3)
    lista2.append(tupla)
print(f"Entrada: lista={lista}\nResultado: {lista2}")