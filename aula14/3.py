'''Contagem de ocorrências: Dado um texto armazenado em uma string,crie um programa que conte a quantidade de ocorrências de cada palavra e retorne uma tupla contendo a palavra e o número de ocorrências.
Exemplo: Para o texto: "A casa é bonita, a casa é azul", a saída seria (('A', 1), ('casa', 2), ('é', 2), ('bonita,', 1), ('azul', 1)). '''
string="A casa é bonita a casa é azul"
t=tuple(string.split())
contador={}
for elemento in t:
    if elemento in contador:
        contador[elemento]+=1
    else:
        contador[elemento]=1
print(tuple(contador.items()))