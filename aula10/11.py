frase=input("Digite uma frase ou uma palavra: ")
fraseCase=frase.lower()

for i in fraseCase:
    casa=fraseCase.count(i)
    print(casa)