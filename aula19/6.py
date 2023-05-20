#Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo. Valores esperados: múltiplo(8, 4) = True; múltiplo(7, 3) = False; múltiplo(5, 5) =True.
def multiplo(n1,n2):
    if n1 % n2 == 0: return True
    else: return False
print(multiplo(5,5))