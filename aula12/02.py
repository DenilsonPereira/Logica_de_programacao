impar=[]
par=[]
for i in range(0,10):
    num=int(input("Digite um número: "))
    if num%2==0:
        par.append(num)
    if num%2!=0:
        impar.append(num)
print(par)
print(impar)