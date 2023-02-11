cont = int(0)

for i in cont<3:
    num = int(input("Digite um numero: "))

    if cont==0:
        maior=num
        menor=num
    if num>maior:
        maior=num
    if num<menor:
        menor=num
    
    cont=cont+1

print(maior, menor)