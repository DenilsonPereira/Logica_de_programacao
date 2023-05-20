#A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15. Crie uma função recursiva para calcular o fatorial duplo de um número n.
def fatorialDuplo(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * fatorialDuplo(n - 2)
print(fatorialDuplo(8))