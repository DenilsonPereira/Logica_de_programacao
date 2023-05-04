n1=int(input("Informe o primeiro valor: "))
n2=int(input("Informe o segundo valor: "))
n3=int(input("Informe o terceiro valor: "))
n4=int(input("Informe o quarto valor: "))
tupla=(n1,n2,n3,n4)
print(f"Você digitou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 not in tupla:
    print("O valor 3 não apareceu em nenhuma posição")
elif 3 in tupla:
    print(f"O primeiro valor 3 foi digitado na  {tupla.index(3)+1}ª posição")
pares=()
for i in tupla:
    if i%2==0:
        pares=pares+(i,)
print(f"Os números pares foram: {pares}")