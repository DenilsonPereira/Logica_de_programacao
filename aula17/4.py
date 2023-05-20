#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverse(num):
    num = str(num)
    num = num[::-1]
    return num
print(reverse(721))