#Defina a função recursiva div que recebe como argumentos dois números naturais m e n e devolve o resultado da divisão inteira de m por n. Neste exercício não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.
def div(m,n):
    #Dados dois números inteiros a e b, (com b > 0), então, existem dois números inteiros q e r (com r > 0), tais que, a=b×q+r
    if n > m: return 0
    else: return 1 + div(m-n,n)
print(div(10,5))