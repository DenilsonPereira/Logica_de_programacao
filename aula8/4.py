#Calcula o fatorial de um número
numero=int(input("Digite um número: "))
resultado = 1
count = 1
while(count<=numero):
    resultado=resultado*count
    count=count+1
print(resultado)