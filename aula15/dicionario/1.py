'''filme={'titulo':'Star Wars', 'ano':1977,'diretor':'George Lucas'}
for k,v in filme.items():
    print(f'O {k} é {v}')
locadora=[{'titulo':'Star Wars', 'ano':1977,'diretor':'George Lucas'}, {'titulo':'Avengers', 'ano':2012,'diretor':'Joss Whedon'},{'titulo':'Matrix', 'ano':1999,'diretor':'Wachowski'}]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])
pessoas={'nome':'Denilson', 'sexo':'M', 'idade':24}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome']='Carlos'
pessoas['peso']=75.2
for k,v in pessoas.items():
    print(k, v)'''
    
estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input("Unidade Federativa: "))
    estado['sigla']=str(input("Sigla do Estado: ")).upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()