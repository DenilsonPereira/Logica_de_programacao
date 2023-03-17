string=input("Digite um texto ou nome: ")
stringRev=0

for i in range(len(string)):
    if stringRev<=0 and stringRev==(-len(string)):
        stringRev=stringRev-1
        print(string[-i-stringRev])