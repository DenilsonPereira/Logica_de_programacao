#Implemente um algoritmo para encontrar o par de elementos distintos em uma lista cuja soma seja igual a um determinado valor X fornecido pelo usuário. Caso a lista não contenha um par, uma mensagem deve ser mostrada para o usuário.
lista=[2,1,3,8,9,7,5]
num=int(input("Informe um número: "))
c=0
for i in lista:
    for j in lista:
        if j!=i:
            if i+j==num:
                print(f"{i}+{j}={num}")
                c+=1
if c==0:
    print(f"Não existe pares que somados dê {num}")