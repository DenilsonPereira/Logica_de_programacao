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
    if opcao==0:
        print("Encerrando!")
        break
    if opcao==1:
        nome=input("Qual o nome? ")
        telefone=input("Digite os telefones separados por virgula: ").split(",")
        agenda[nome]=telefone
        print("Adicionado com sucesso!")
    elif opcao==2:
        nome=input("Digite o nome: ")
        if nome in agenda:
            telefone=input("Digite o telefone que deseja adicionar: ")
            agenda[nome].append(telefone)
        else:
            opcao=input("Nome não encontrado, deseja adicionar? (S/N)").lower()
            if opcao=="s":
                telefone=input("Digite os telefones separados por vírgulas: ").split(",")
                agenda[nome]=telefone
                print("Nome adicionado com sucesso!")
    elif opcao==3:
        nome=input("Informe o nome: ")
        if nome in agenda:
            if len(agenda[nome])==1:
                opcao=input(f"{nome} tem apenas um telefone. Deseja excluir da agenda? (S/N)").lower()
                if opcao=="s":
                    agenda.pop(nome)
                    print("Nome excluido com sucesso!")
                else:
                    telefone=input("Informe o telefone: ")
                    agenda[nome].remove(telefone)
                    print("Telefone removido com sucesso!")
            else: print("Nome não encotrado!")
    elif opcao==4:
        nome=input("Informe o nome: ")
        if nome in agenda:
            agenda.pop(nome)
            print("Nome removido com sucesso!")
        else: print("Nome não encontrado!")
    elif opcao==5:
        nome=input("Informe o nome: ")
        if nome in agenda:
            print(agenda[nome])
            print("Telefones: ", ",".join(agenda[nome]))
        else: print("Nome não encontrado!")
    else: print("Opção inválida!")