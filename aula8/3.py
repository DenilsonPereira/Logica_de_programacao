#Imprime quantos números pares existem entre os números informados
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s=n1
i=0
while(n1<n2):
    n1=n1+1
    if n1%2==0:
        i=i+1 
print(i)