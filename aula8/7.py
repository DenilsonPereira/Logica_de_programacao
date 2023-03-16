filhos=0
salario=0.0
media=0.0
soma=0.0
dividir=0.0
pessoas=0
percentual=0.0
pessoa150=0
mediaSalario=0.0
mediaFilhos=0.0
maiorSalario=0.0


while(pessoas>=0):
    filhos=int(input("Informe quantos filhos: "))
    salario=float(input("Informe o salário: "))
    
    soma=soma+salario
    dividir=dividir+filhos
    pessoas=pessoas+1
    if(salario>=0 and salario<=150):
        pessoa150 = pessoa150+1
    if(salario>maiorSalario):
        maiorSalario=salario
    if(salario<0):
        break
    if(pessoas>0):  
        mediaFilhos=dividir/pessoas
        mediaSalario=soma/pessoas
        percentual=(pessoa150/pessoas)*100

print(f"A média dos salários da população ({pessoas}) é {mediaSalario}")
print(f"A média do número de filhos é {mediaFilhos}")
print(f"O maior salário é {maiorSalario}")
print(f"O percentual de pessoas com salário até R$150,00 é de {percentual}")
