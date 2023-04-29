'''
Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve conter um menu onde dependendo da entrada do usuário, será possível:
- incluir Novo Nome 
- acrescenta um novo nome na agenda, com um ou mais telefones.
- incluir Telefone
- acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. - excluirTelefone 
- exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. 
- excluirNome 
- exclui uma pessoa da agenda. 
- consultarTelefone
- retorna os telefones de uma pessoa na agenda.'''
agenda = {}

while True:
    print("1 - Incluir novo nome")
    print("2 - Incluir telefone")
    print("3 - Excluir telefone")
    print("4 - Excluir nome")
    print("5 - Consultar telefone")
    print("0 - Sair")
    
    opcao=int(input("Escolha a opção: "))
    if opcao==1:
        nome=input("Qual o nome? ")
        nomes={nome,}
        agenda.update(nomes)