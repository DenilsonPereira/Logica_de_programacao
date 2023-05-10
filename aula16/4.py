#Dado um dicionário de palavras e suas traduções em diferentes idiomas (considere inglês, português, espanhol e francês), como você encontraria todas as palavras que começam comum a determinada letra(considere chaves e valores)?
d={'abacate':['avocado', 'avocat'], 'bola':['bola','ball', 'balle'], 'casa':['house', 'loger', 'coisa']}
letra=input("Palavras com qual letra: ")
for k,v in d.items():
    if k.startswith(letra):
        print(k)
    for i in v:
        if i.startswith(letra):
            print(i)