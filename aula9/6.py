num=int(input("Informe um número: "))
tab = 0
for i in range(1,11):
    tab = num*i
    print("{0} X {1} = {2}".format(num,i,tab))