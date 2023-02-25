#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

altura = float(input("Sua altura: "))
#a. Para homens: (72.7*h) - 58 
pesoHomem = (72.7*altura)-58

#b. Para mulheres: (62.1*h) - 44.7
pesoMulher = (62.1*altura)-44.7

print(f"Se você for Homem, seu peso ideal é {pesoHomem:.2f} \nSe você for Mulher, seu peso ideal é {pesoMulher:.2f}")