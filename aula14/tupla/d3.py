import random
tupla=()
for i in range(5):
    d=int(random.randrange(0,99))
    tupla=tupla+(d,)
print(f"Tupla: {tupla}\nMenor valor: {min(tupla)}\nMaior valor: {max(tupla)}")