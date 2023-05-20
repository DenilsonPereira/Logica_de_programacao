#Escreva uma função que recebe como entrada um número ano e retorna True caso ano seja bissexto. Caso contrário, retorne False. Help: https://learn.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year
ano=int(input("Informe um ano: "))
def bissexto(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return True
            else: return False
        else: return False
    else: return False
print(bissexto(ano))