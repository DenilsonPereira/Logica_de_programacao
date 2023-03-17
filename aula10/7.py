data = input("Informe uma data: (00/00/0000): ")
#data1=data.replace(data.find("0"), "de")
if data[0:4]=="0" and data[0:5]=="1":
    mes=str(janeiro)
print(data[0:2], "de ",mes, " de", data[-4:] )