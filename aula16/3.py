#Escreva uma função que receba uma lista de números inteiros e retorne uma lista contendo apenas os números primos.
lista = []
primos = []
nao = []
for i in range(1, 101):
    lista.append(i)
for i in lista:
    nao_atual = []
    if i>1:
        for c in range(2, i):
            if i%c == 0:
                nao_atual.append(i)
                break
        if len(nao_atual) == 0: primos.append(i)
    else: nao.append(i)
print(primos)