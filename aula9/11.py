numero=int(input("Informe um número: "))
fatorial=1
count=numero
print(f"Fatorial de: {numero}")
print(f"{numero}! = ", end="")
for i in range(count-1):
    fatorial=fatorial*count
    count=count-1
    print(count, end=" * ")
print(f" = {fatorial}")