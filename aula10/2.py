nome = input("Digite seu nome: ")
for i in range(len(nome)):
    nomeRev=nome[-i-1]
    print(nomeRev.upper(), end="")