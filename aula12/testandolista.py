lista=[1,2,8,9,7,8,0]
print(lista)
lista[6]=10
print(lista)
ls=[20,15]
lista= lista+ls
print(lista)
lista=[0,1,2,3,4,5,6,7,8,9,10]
print('Lista antes remoção: ', lista)
lista[2:3]=lista[5:6]
print('Lista depois da remoção: ', lista)
del lista[0]
print(lista)