num = int(input("Informe um número inteiro: "))

cent = 0
deze = 0
unid = 0

if num<1000:
    cent = int(num/100)
    deze = int((num-(cent*100))/10)
    unid = int(num-(cent*100)-(deze*100)/10)
    print(f"{num} = {cent} centena(s), {deze} dezena(s) e {unid} unidade(s)")