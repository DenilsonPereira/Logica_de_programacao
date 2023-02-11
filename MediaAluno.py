nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2

if media>=7 and media<=9.9:
    print("APROVADO")
elif media==10:
    print("APROVADO com Distinção")
else:
    print("REPROVADO")