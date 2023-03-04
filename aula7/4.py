precoProd = float(input("Informe o preço do produto: "))
codigo = int(input("Informe o código de pagamento: "))

if codigo==1:
    print(f"O valor a pagar é: R${precoProd-((precoProd*10)/100)}")
elif codigo==2:
    print(f"O valor a pagar é: R${precoProd-((precoProd*15)/100)}")
elif codigo==3:
    print(f"O valor a pagar é: R${(precoProd)}")
elif codigo==4:
    print(f"O valor a pagar é: R${precoProd+((precoProd*10)/100)}")
elif codigo==5:
    print(f"O valor a pagar é: R${precoProd+((precoProd*20)/100)}")