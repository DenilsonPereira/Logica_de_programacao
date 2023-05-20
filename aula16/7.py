'''Desenvolva um jogo da forca.
-O programa deverá ter um repositório de palavras armazenadas em uma estrutura, contendo “palavra” e “dica”.
-O programa deverá escolher aleatoriamente cada palavra e a dica deverá ser mostrada ao usuário.
-O jogador poderá errar 6 vezes antes de ser enforcado.'''
import random
palavras = [{'palavra':'brasil', 'dica':'País'},
          {'palavra':'sushi', 'dica':'É do japão'},
          {'palavra':'peixe', 'dica':'Vive na água'}]

dicas = random.choice(palavras)
dica = dicas.keys()
palavra_secreta = list(dicas['palavra'])
print('-'*15, 'Jogo da Forca', '-'*15)
print(f"Dica: {dicas['dica']}")

letras_descobertas = []

for i in range(0, len(palavra_secreta)):
    letras_descobertas.append('-')

errou = 0

while True:
    letra = str(input("\nDigite uma letra: ")).lower()
    
    if letra not in palavra_secreta:
        errou += 1
        if errou < 6:
            print(f"Você errou pela {errou}ª vez. Tente de novo!")
    else:
    
        for i in range(0, len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                letras_descobertas[i] = letra
            print(letras_descobertas[i], end="")
            
        if letras_descobertas == palavra_secreta:
            print(f"\nParabéns, você acertou a palavra!\nA palavra era {dicas['palavra'].upper()}")
            break
    if errou == 6:
        print("Você foi ENFORCADO!")
        break