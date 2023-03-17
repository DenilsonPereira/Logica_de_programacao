data = input("Informe sua data de nascimento no formato dd/mm/aaaa: ")
dia=data[0:2]
mes=data[3:4]+data[4:5]
ano=data[-4:]
print("Você nasceu em", dia, end=" ")
if mes=="01":
    print("de Janeiro de", ano )
elif mes=="02":
    print("de Fevereiro de",ano )
elif mes=="03":
    print("de Março de", ano)
elif mes=="04":
    print("de Abril de", ano) 
elif mes=="05":
    print("de Maio de", ano)
elif mes=="06":
    print("de Junho de", ano) 
elif mes=="07":
    print("de Julho de", ano)
elif mes=="08":
    print("de Agosto de", ano)
elif mes=="09":
    print("de Setembro de", ano)
elif mes=="10":
    print("de Outubro de", ano)
elif mes=="11":
    print("de Novembro de", ano)
elif mes=="12":
    print("de Dezembro de", ano)