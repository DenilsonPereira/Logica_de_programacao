metros = int(input("Informe quantos metros quadrados: "))
lataLitros = 18
custoLata= 80
coberturaLitros = metros/3

latas = coberturaLitros/lataLitros
custo = latas*custoLata

if latas%54 == 0:
    print(f"A quantidade de latas de tintas necessárias é {latas:.2f}")
elif latas%54 != 0:
    print(f"A quantidade de latas de tintas necessárias é {(latas+1):.1f}")


print(f"E o valor é {custo:.2f}")
