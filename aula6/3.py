idade = int(input("Digite sua idade: "))

if ((idade>=5) and (idade<=7)):
    print("infatil A")
elif((idade>=8) and (idade<=10)):
    print("infatil B")
elif((idade>=11) and (idade<=13)):
    print("juvenil A")
elif((idade>=14) and (idade<=17)):
    print("juvenil B")
elif((idade>=18)):
    print("adultos")
else:
    print("Não aceito")