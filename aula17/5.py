#Faça uma função que retorne a quantidade de dígitos de um determinado número inteiro informado pelo usuário. Não realize conversão de tipos
def tamanho(num):
    if not(type(num)==int):
        return
    c=0
    while num>0:
        num//=10
        c+=1
    return c
print(tamanho(2023))