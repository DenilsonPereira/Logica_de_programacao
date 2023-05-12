#Utilizando funções, leia um número inteiro e retorne o seu equivalente em numeração romana.
def romanos(numero):
    num = (1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000)
    rom = ("I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M")
    count=12
    while numero!=0:
        divisao=numero//num[count]
        numero%=num[count]
  
        while divisao:
            print(rom[count], end = "")
            divisao -= 1
        count -= 1

number =int(input("Qual o numero: "))
romanos(number)