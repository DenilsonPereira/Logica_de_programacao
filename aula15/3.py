#Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes e acesse os dados dos dicionários.
filmes={'Batman Forever':{'Duas Caras': '1995'}, 'Dr Estranho 2': {'Karl Mordo':'2016'}, 'Homem-Aranha: Longe de Casa':{'Mysterio':'2019'}, 'Duro de Matar':{'Hans Gruber':'1988'}, 'Vingadores: Ultimato':{'Thanos':'2019'}}
print(filmes.keys())
print(filmes.values())
for filme in filmes:
    print(f"{filme} -> {filmes[filme]}")
while True:
    des=input("Deseja pesquisar (s/n)? ")
    if des=='n':
        break
    nome=input("Qual o nome do filme? ")
    if nome in filmes: 
        print(filmes[nome])
        break
    if nome not in filmes: nome=input("Qual o nome do filme? ")