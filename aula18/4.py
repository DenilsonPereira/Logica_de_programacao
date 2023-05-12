#Modifique a questão anterior de forma que as vogais da string não sejam embaralhadas, ou seja, permaneçam na mesma posição.

palavra=input("Informe uma palavra: ").upper()

def embaralhar(string):
    import random
    consoante=[]
    for i,line in enumerate(string):
        if line not in 'AEIOU':
            consoante.append(i)
            
    random.shuffle(consoante)
    consoante=iter(consoante)
    novaPalavra=""
    for i,line in enumerate(string):
        if line not in 'AEIOU':
            novaPalavra+=string[next(consoante)]
        else:
            novaPalavra+=line
            
    print(novaPalavra)
    
embaralhar(palavra)