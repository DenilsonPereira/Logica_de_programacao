#Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está usando como valor.
pessoas={'Ryan': 'Branca', 'Marcelo': 'Preto', 'Beatriz': 'Preto', 'Juan': 'Vinho', 'Washington': 'Vermelho'}
for pessoa in pessoas:
    print(f"{pessoa} = {pessoas[pessoa]}")