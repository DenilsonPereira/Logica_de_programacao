def ls(n):
    if len(n) ==1: #verificando se a lista possui apenas 1 elemento
        return n[0]
    else:
        return n[0] + ls(n[1:]) # a função chama a si mesma
print(ls([2,4,6,8,10]))