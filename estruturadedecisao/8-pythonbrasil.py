#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
prod1 = float(input("Valor do primeiro produto: R$"))
prod2 = float(input("Valor do segundo produto: R$"))
prod3 = float(input("Valor do terceiro produto: R$"))

if prod1<prod2 and prod1<prod3:
    print("O produto que você deve comprar é o primeiro, custa R${}".format(prod1))
elif prod2<prod1 and prod2<prod3:
    print("O produto que você deve comprar é o segundo, custa R${}".format(prod2))
elif prod3<prod1 and prod3<prod2:
    print("O produto que você deve comprar é o terceiro, custa R${}".format(prod3))
elif prod1==prod2 and prod1<prod3:
    print("O primeiro e o segundo estão com o mesmo preço R${}, descida qual deles levar".format(prod1))
elif prod2==prod3 and prod2<prod1:
    print("O segundo e o terceiro estão com o mesmo preço R${}, descida qual deles levar".format(prod2))
elif prod3==prod1 and prod3<prod2:
    print("O primeiro e o terceiro estão com o mesmo preço R${}, descida qual deles levar".format(prod3))