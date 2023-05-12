#Escreva um programa que determine o menor número inteiro positivo que pode ser dividido por todos os números de 1 a 20 sem deixar resto
numero=1
div=False

while not div:
    div=True
    for i in range(1,21):
        if numero%i!=0:
            div=False
            break
    if not div:
        numero+=1
print(numero)