#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e‘N’ ,se seu argumento for zero ou negativo.
def positivoNegativo(num):
    if num>0:
        num='P'
    else:
        num='N'
    return num
print(positivoNegativo(-2))