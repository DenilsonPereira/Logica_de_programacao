numero1=int(input("Informe um número: "))
numero2=int(input("Informe um número: "))

count = 0

for i in range(numero1,numero2):
    numero1=numero1+1
    if numero1%2!=0:
        count= count+1
print(count)