#Faça uma função que computa a potência de a^b para valores de a e b informados pelo usuário. Assuma valores de a e b como inteiros e não utilize o operador ** ou funções da biblioteca Math.
def potencia(a,b):
    auxiliar=1
    for i in range(b):
        auxiliar*=a
    return auxiliar
print(potencia(4,1))