idades=[]
alturas=[]
inf=0
i=0
while True:
    idade=int(input("Idade: "))
    if idade<0:
        break
    altura=float(input("Altura: "))
    if altura<0:
        break
    idades.append(idade)
    alturas.append(altura)
    i=i+1
c=0
while c<i:
    medias=sum(alturas)/4
    if idades[c]>13:
        alt=alturas[c]
        if alt<medias:
            inf=inf+1
    else:
        print()
    c=c+1

print(f'Altura média: {medias}m')
print(f'Alunos com mais de 13 anos que possuem altura inferior a média: {inf}')