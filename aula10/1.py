p1 = input("Digite uma palavra ou um texto: ")
p2 = input("Digite uma palavra ou um texto: ")

print(p1, ". Comprimento:",len(p1))
print(p2, ". Comprimento:",len(p2))
if (len(p1) == len(p2)) and (p1==p2):
    print("Mesmo comprimento e mesmo conteúdo")
elif(len(p1)==len(p2) and (p1!=p2)):
    print("Mesmo comprimento e conteúdo diferente")
else:
    print("Comprimento diferente e conteúdo diferente")

