'''Escreva uma função em que dada uma tupla, remova os valores duplicados. 
Exemplo: tupla = (1, 3, 5, 2, 3, 5, 1, 1, 3)
Resultado: A tupla original é: (1, 3, 5, 2, 3, 5, 1, 1, 3)
A tupla após a remoção de duplicatas: (1, 2, 3, 5)
Obs: Não converter a tupla para nenhum outro tipo.
'''
t=(1, 3, 5, 2, 3, 5, 1, 1, 3)
print("A tupla original é: ",t)

t1=tuple()
for i in range(len(t)):
    if t[i] not in t1:
        t1+=(t[i],)
print("A tupla após a remoção de duplicatas: ",t1)