#Escreva uma função que recebe como entrada um número ano e retorna True caso ano seja bissexto. Caso contrário, retorne False. Help: https://learn.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year
def bissexto(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0: return True
    else: return False
print(bissexto(1900))