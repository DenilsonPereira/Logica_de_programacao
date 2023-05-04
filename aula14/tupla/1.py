'''lanche=("Hamburguer", "Suco", "Pizza", "Pudim")
#Tuplas são imutáveis
print(lanche[2])
print(lanche[1:3])
print(lanche[-2])
for c in lanche:
    print(c)
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
for p,c in enumerate(lanche):
    print(f"{p} -> {c}")'''
a=(2,5,4)
b=(5,8,1,2)
c=a+b
print(c)