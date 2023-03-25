data=list(input("Digite a data de nascimento no formato dd/mm/aaaa? "))
mes=['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
ano=data[6]+data[7]+data[8]+data[9]
m=int(data[3])
n=int(data[4])
if n==1:
    meses=mes[0]
if n==2:
    meses=mes[1]
if n==3:
    meses=mes[2]
if n==4:
    meses=mes[3]
if n==5:
    meses=mes[4]
if n==6:
    meses=mes[5]
if n==7:
    meses=mes[6]
if n==8:
    meses=mes[7]
if n==9:
    meses=mes[8]
if m==1 and n==0:
    meses=mes[9]
if m==1 and n==1:
    meses=mes[10]
if m==1 and n==2:
    meses=mes[11]
print(f"Você nasceu em {data[0]}{data[1]} de {meses} de {ano}")