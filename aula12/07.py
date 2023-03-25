mes=['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas=[]
for i in range(12):
    print(f"Mês: {mes[i]}")
    temp=float(input("Qual a temperatura do mês?"))
    temperaturas.append(temp)
    #print(temp)
media=sum(temperaturas)/len(temperaturas)
print(f"Média anual: {media:.4}°C")
for c in range(12):
    if temperaturas[c]<media:
        print(f"{c+1} - {mes[c]}", end=", ")
#print(temperaturas)