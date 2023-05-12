#Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes e acesse os dados dos dicionários.
filmes={'Batman Forever':{'Duas Caras': '1995'},
        'Dr Estranho 2': {'Karl Mordo':'2016'}, 
        'Homem-Aranha: Longe de Casa':{'Mysterio':'2019'}, 
        'Duro de Matar':{'Hans Gruber':'1988'}, 
        'Vingadores: Ultimato':{'Thanos':'2019'}}

while True:
    des=input("Deseja pesquisar (s/n)? ").lower()
    if des=='n':
        break
    if des=='s':
        nome=input("Qual o nome do filme? ")
       
        if nome in filmes: 
            vilao=list(filmes[nome].keys())[0]
            ano=filmes[nome][vilao]
            print(f"Filme: {nome}\nVilão: {vilao}\nAno de lançamento: {ano}")
            break
        else: nome=input("Qual o nome do filme? ")
    else: print("Entrada inválida!")