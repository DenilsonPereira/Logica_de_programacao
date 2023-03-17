num=int(input("Informe um número: "))
ultimo=1
penultimo=1

if(num<=500):
    print(penultimo, ultimo, end=" ")
    if(num==1 or num==2):
        print("1")
    else:
        for i in range(2,num):
            termo=ultimo+penultimo
            penultimo=ultimo
            ultimo=termo
            i+=1
            print(termo, end=" ")
else:
    print("O valor é maior que 500")