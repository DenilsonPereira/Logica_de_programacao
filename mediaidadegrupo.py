#usar array para tentar melhorar a solução
i1 = 10
i2 = 12
i3 = 15
i4 = 17
i5 = 16

mediaA = (i1+i2+i3+i4)/4
mediaP = (i1+i2+i3+i4+i5)/5
variacao = ((mediaP/mediaA)-1)*100

print("A media de idade do grupo é: ", mediaA,". E a variação percentual ao incluir uma pessoa de ", i5, "é de:", variacao)