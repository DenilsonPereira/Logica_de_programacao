"""A prefeitura de uma cidade deseja fazer uma pesquisa entre seus
habitantes. Faça um algoritmo para coletar e armazenar dados sobre
o salário e número de filhos de cada habitante e após as leituras,
escrever:
numFilhos=0
numSalarios=0
numPessoas=0
salarioPessoas150=0
salario=0.0
porcentagemSalario=0.0
maiorSalario=0.0
mediaSalario=0.0
mediaFilhos=0.0

while(numPessoas>=0):
    numFilhos=int(input("Digite o número de filhos: "))
    numSalarios=int(input("Digite o valor do salário: "))
    if(numFilhos<0):
        break
    numPessoas=numPessoas+1
    if(salario>maiorSalario):
        maiorSalario=salario
    if(salario<=150.0):
        salarioPessoas150=salarioPessoas150+1
    mediaSalario=salario+1
    mediaFilhos=numFilhos+1
if(numPessoas):
    mediaSalario=mediaSalario/numPessoas
    mediaFilhos=mediaFilhos/numPessoas
    porcentagemSalario=(salarioPessoas150/numPessoas)*100


print(f"A média dos salários da população ({numPessoas}) é {mediaSalario}")
print(f"A média do número de filhos é {mediaFilhos}")
print(f"O maior salário é {maiorSalario}")
print(f"O percentual de pessoas com salário até R$150,00 é de {porcentagemSalario}")"""
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