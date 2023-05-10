#Escreva um programa que receba uma lista de palavras como argumento e retorne um dicionário onde as chaves são as palavras únicas e os valores são a contagem de ocorrências de cada palavra.
lista=['casa', 'lanche', 'coisa', 'casa', 'arvore']
dicionario={}
for i in range(len(lista)):
    dicionario[lista[i]]=lista.count(lista[i])
print(dicionario)