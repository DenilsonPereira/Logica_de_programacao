#gerador de tabuada
n=int(input("Digite um numero: "))
i = 0
print(f"Tabuada de {n}:")
while(i<10):
    if n<=10 and n>=-10:
        i = i + 1
        print(f"{n} X {i} = {n * i}")
    else:
        break