numero=int(input("Informe um número: "))
fatorial=1
count=numero
for i in range(count):
    fatorial=fatorial*count
    count=count-1
print(fatorial)