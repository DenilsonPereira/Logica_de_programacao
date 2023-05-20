#Escreva uma função que receba um número de parâmetros indefinido. Imprima a quantidade de parâmetros recebidos de cada tipo de dado. A função também deve imprimir o maior e o menor valor numérico recebido.
def parametros(*valor):
    new=[]
    s=0
    i=0
    f=0
    b=0
    for j in range(len(valor)):
        if type(valor[j])==str:
            s+=1
        elif type(valor[j])==int:
            i+=1
        elif type(valor[j])==float:
            f+=1
        elif type(valor[j])==bool:
            b+=1
        if type(valor[j])==int or type(valor[j])==float:
            new.append(valor[j])
    print(f"String: {s}\nInteiro: {i}\nFloat: {f}\nBooleano: {b}")
    print(f"Maior valor númerico: {max(new)}")
    print(f"Menor valor númerico: {min(new)}")
    return valor
parametros(1,2,'a', 5.2, True)