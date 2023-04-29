#Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).
aulas=['Logica de matematica', 'Inovacão e Startup', 'Fundamentos da informática', 'Inglês', 'Lógica de Programação']
nao=[]
semana={'Domingo':nao, 'Segunda':nao, 'Terça':aulas[0:2], 'Quarta':aulas[2:4], 'Quinta':aulas[4], 'Sexta':aulas[4], 'Sábado':nao}
for dias in semana:
    print(f"{dias} -> {semana[dias]}")