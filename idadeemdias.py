print("Informe sua idade em anos, meses e dias, e obtenha ela em dias.")
anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

idade = ((anos*365)+(meses*30)+dias)
print("Idade em dias: ", idade, "dias")