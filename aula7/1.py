peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso/(altura**2)

if imc<20:
    print("Abaixo do normal")
elif imc>=20 and imc<25:
    print("Normal")
elif imc>=25 and imc<30:
    print("Sobrepeso")
elif imc>=30 and imc<35:
    print("Obesidade leve")
elif imc>=35 and imc<40:
    print("Obesidade moderada")
elif imc>=40:
    print("Obesidade mórbida")