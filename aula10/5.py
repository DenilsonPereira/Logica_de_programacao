string=input("Digite uma sequência de caracteres: ")
stringC=string.replace(' ', "")
"""
stringC=string.replace('´', "")
stringC=string.replace('^',"")
stringC=string.replace('~',"")
"""
print(stringC)
stringRev=stringC[::-1]
print(stringRev)
if stringC==stringRev:
    print("É PALÍDROMO")
else:
    print("NÃO É PALÍDROMO")