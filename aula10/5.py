import unicodedata
string=input("Digite uma sequência de caracteres: ")
stringC=string.replace(' ', "")
"""
stringC=string.replace('é', "")
stringC=string.replace('â',"")
stringC= ''.join(ch for ch in unicodedata.normalize('NFKD', string) 
    if not unicodedata.combining(ch))
stringC=string.replace('ã',"")"""

print(stringC)
stringRev=stringC[::-1]
print(stringRev)
if stringC==stringRev:
    print("É PALÍDROMO")
else:
    print("NÃO É PALÍDROMO")