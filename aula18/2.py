'''
Faça um programa de implemente um jogo de Craps. 
- O jogador lança um par de dados, obtendo um valor entre 2 e 12.
- Se, na primeira jogada, você tirar 7 ou 11, você tirou um "natural" e ganhou. 
- Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
- Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
import random

d1=[1,2,3,4,5,6]
d2=d1

natural=[7,11]
craps=[2,3,12]
ponto=[4,5,6,8,9,10]

def crap():
    pontos=0
    rodada=0
    while True:
        valor=random.randint(d1[0],d1[5])+random.randint(d2[0],d2[5])
        rodada+=1
        if rodada==1:
            if valor in natural: 
                print(f"{valor}, você tirou um natural e GANHOU!")
                break
            elif valor in craps: 
                print(f"{valor}, deu CRAPS você PERDEU!")
                break
            elif valor in ponto: 
                pontos=valor
                print(f"{valor}, voce fez PONTO")
        elif rodada>1:
            if pontos==valor:
                print(f"Você tirou {valor} novamente e GANHOU!")
                break
            if valor==natural[0]:
                print(f"Você tirou {valor} e PERDEU!")
                break

crap()