'''Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
-Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
-Padronize em sua função para que todos os caracteres sejam devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''
st=input("Informe uma palavra: ").upper()

def embaralhar(string):
    import random
    lista=list(string)
    for line in string:
        line=lista
        random.shuffle(line)
        result=''.join(line)
    print(result)
    
embaralhar(st)