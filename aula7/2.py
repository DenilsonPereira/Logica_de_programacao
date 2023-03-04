num = float(input("Informe um número: "))

if num%3==0 and num%4!=0:
    print("É divisível por 3")
if num%4==0 and num%3!=0:
    print("É divisível por 4")
if num%3==0 and num%4==0:
    print("É divisível tanto por 3 quanto por 4")