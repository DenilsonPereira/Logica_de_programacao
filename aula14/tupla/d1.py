num=('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
digitado=int(input("Digite um número entre 0 e 20: "))
while True:
    if digitado>=0 and digitado<=20: 
        print(f"Você digitou o número {num[digitado]}")
        break
    elif digitado<0:
        digitado=int(input("Tente novamente! Digite um número entre 0 e 20: "))
    elif digitado>20:
        digitado=int(input("Tente novamente! Digite um número entre 0 e 20: "))