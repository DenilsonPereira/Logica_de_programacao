#Faça uma função que retorne a quantidade de dígitos de um determinado número inteiro informado pelo usuário. Não realize conversão de tipos
def tamanho(num):
    c=0
    while num>0:
        num=num//10
        c+=1
    return c
print(tamanho(9562))