n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

if ((n1>n2) and (n1>n3) and (n2>n3)):
    print(n1, n2, n3)
elif ((n1>n3) and (n1>n2) and (n3>n2)):
    print(n1,n3,n2)
elif ((n2>n3) and (n2>n1) and (n3>n1)):
    print(n2,n3,n1)
elif ((n2>n1) and (n2>n3) and (n1>n3)):
    print(n2,n1,n3)
elif ((n3>n1) and (n3>n2) and (n1>n2)):
    print(n3,n1,n2)
elif ((n3>n1) and (n3>n2) and (n2>n1)):
    print(n3,n2,n1)