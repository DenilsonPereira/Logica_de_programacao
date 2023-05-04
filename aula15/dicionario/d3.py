ctps={}
ctps['nome']=input("Nome: ")
ctps['idade']=2023-(int(input("Ano de Nascimento: ")))
ctps['carteira']=int(input("Carteira de Trabalho (0 não tem): "))
if ctps['carteira']==0:
    print('-='*20)
    print(f"nome tem o valor {ctps['nome']}\nidade tem o valor {ctps['idade']}\nctps tem o valor {ctps['carteira']}\n")
else:
    ctps['contratacao']=int(input("Ano de Contratação: "))
    ctps['salario']=float(input("Salário: "))
    ctps['aposentadoria']=(35-(2023-ctps['contratacao']))+ctps['idade']
    print('-='*20)
    print(f"nome tem o valor {ctps['nome']}\nidade tem o valor {ctps['idade']}\nctps tem o valor{ctps['carteira']}\nsalário tem o valor {ctps['salario']}\naposentadoria tem o valor {ctps['aposentadoria']}\n")