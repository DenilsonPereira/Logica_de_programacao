#Crie uma função geradora da sequência de Fibonacci até o n-ésimo termo.
def fibonacci(n):
    ultimo = 1
    penultimo = 1
    termo = 0
    if n < 2: print(ultimo)
    print(ultimo, penultimo, end=" ")
    for i in range(n-2):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo, end=" ")
    n = ''
    return n

numero = int(input("Informe um número: "))
print(fibonacci(numero))