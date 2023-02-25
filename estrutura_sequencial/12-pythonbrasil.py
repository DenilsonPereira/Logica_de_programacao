#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Sua altura: (ex.: 1.80)"))
peso = (72.7*altura)-58

print(f"{peso:.2f}")