import random
jogador={}
c=0
for i in range(0, 4):
    jogador['jogador'+str(i+1)]=random.randint(1,6)
print("Valores sorteados:")
for k,v in jogador.items():
    print(' '*2,f"O {k} tirou {v}")
print("Ranking dos jogadores: ")
for i in sorted(jogador, key=jogador.get, reverse=True):
    c+=1
    print(' '*2,f"{c}º lugar: {i} com {jogador[i]}")