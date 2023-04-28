'''Registro de alunos: Crie um programa que registre os dados dos alunos de uma turma, incluindo nome, idade e notas. Utilize uma lista de tuplas para armazenar os registros dos alunos e permita a busca de um aluno pelo nome.'''
alunos=[]

while True:
    tem=input("Quer cadastrar o aluno? s para cadastrar ou n para sair: ")
    if tem=='n':
        break
    nome=input("Qual o nome? ")
    idade=int(input("Qual a idade? "))
    n1=float(input("Qual a nota 1? "))
    n2=float(input("Qual a nota 2? "))
    alunos.append((nome, idade, n1, n2))
while True:
    buscar=input("Procurar algum aluno? Digite o nome ou n para sair. ")
    if buscar=='n':
        break
    encontrado=False
    for aluno in alunos:
        if aluno[0]==buscar:
            encontrado=True
            print(f"Nome: {aluno[0]}\nIdade: {aluno[1]}\nNota 1: {aluno[2]}\nNota 2: {aluno[3]}")
            break
        if not encontrado:
            print("Não encontrado!")
    