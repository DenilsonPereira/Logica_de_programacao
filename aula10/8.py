primeira=input("Digite: ")
segunda=input("Digite: ")

posicao=primeira.find(segunda)
if posicao<0:
    print(f"Não há o elemento {segunda} em {primeira}")
elif posicao>0:
    print(f"{segunda} encontrado na posição {posicao} de {primeira}")