dicio=dict()
dicio['Chave 1']=1
dicio['Chave 2']=2
print(dicio)
telefones={'Lucas':'(81)9523-6587', 'Joao':'(89)9785-1236'}
telefones_aux={'Pedro': '(11)9312-9654', 'Ramon': '(21)8795-3654'}
print(telefones)
print(telefones_aux)
telefones.update(telefones_aux)
print(telefones['Joao'][:])
for i in range(0,13):
    print(telefones['Joao'][:-i])

#printando a chave

for telefone in telefones:
    print(telefone)
print(telefones.keys())
print(set(telefones.keys()))

#printando o valor da chave

for telefone in telefones:
    print(f"{telefone} -> {telefones[telefone]}")
print(telefones.values())

#remover um elemento

print(telefones)
telefones.pop('Joao')
print(telefones)
del telefones['Ramon']
print(telefones)

#verificar se um elemento existe
print(telefones.get('Lucas', "Não existe no dicionário"))

#verificar o tamanho do dicionário
print(len(telefones))