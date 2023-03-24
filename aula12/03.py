idades=[]
alturas=[]
inf=0
for i in range(4):
    idade=int(input("Idade: "))
    altura=float(input("Altura: "))
    idades.append(idade)
    alturas.append(altura)
for c in range(i+1):
    medias=sum(alturas)/4
    if idades[c]>13:
        alt=alturas[c]
        if alt<medias:
            inf=inf+1
print(f'Altura média: {medias}m')
print(f'Alunos com mais de 13 anos que possuem altura inferior a média: {inf}')