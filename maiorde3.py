num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

if ((num1>num2) and (num1>num3)):
    print(num1)
elif ((num2>num1) and (num2>num3)):
    print(num2)
elif((num3>num1) and (num3>num2)):
    print(num3)