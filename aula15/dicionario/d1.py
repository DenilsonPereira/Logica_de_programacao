aluno={}
aluno['Nome']=input("Nome: ")
aluno['Média']=int(input(f"Média de {aluno['Nome']}: "))
if aluno['Média']>=7:
    aluno['Situação']='aprovado'
elif aluno['Média']<7:
    aluno['Situação']='reprovado'
print(f"Nome é igual {aluno['Nome']}\nMédia é igual a {aluno['Média']}\nSituação é igual a {aluno['Situação']}")