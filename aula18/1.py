'''Faça um programa que converta da notação de 24 horas para anotação de 12 horas.
-Por exemplo, o programa deve converter 14:25 em 2:25P.M.
-A entrada é dada em dois inteiros.
-Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída
-Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''

def formathour(h,m):
    if h>=0 and h<13:
        print(f"{h}:{m} A.M.")
    if h>13 and h<=24:
        conversao(h,m)
    if h>25:
        print("Hora invalida, realize uma nova consulta!")

def conversao(hora,m):
    pm={13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11, 24:12}
    for k,v in pm.items():
        if k==hora:
            print(f"{v}:{m} P.M")

while True:
    hora=int(input("Informe a hora: "))
    minuto=int(input("Informe os minutos: "))

    formathour(hora,minuto)
    continuar=input("Quer realizar uma nova conversão? (S/N)").upper()
    if continuar=="N":
        break