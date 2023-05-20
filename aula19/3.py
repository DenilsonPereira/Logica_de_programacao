#Escreva uma função que recebe um número como parâmetro e para cada número menor que o parâmetro, a função imprime "Fizz" se o número for múltiplo de três, imprime "Buzz" se o número for múltiplo de cinco, e imprime "FizzBuzz" se o número for múltiplo de três e cinco. Caso o número não seja múltiplo nem de três nem de cinco, ele deve ser impresso.
n=int(input("Informe: "))
def fizz(n):
    if (n % 3 == 0) and (n % 5 == 0): return "FizzBuzz"
    elif n % 3 == 0: return "Fizz"
    elif n % 5 == 0: return "Buzz"
    else: return n

print(fizz(n))