num=int(input("Informe um numero: "))
ultimo=1
penultimo=1

print(penultimo, ultimo, end=" ")

if(num==1 or num==2):
    print("1")
else:
    for count in range(2,num):
        termo=ultimo+penultimo
        penultimo=ultimo
        ultimo=termo
        count+=1
        print(termo, end=" ")