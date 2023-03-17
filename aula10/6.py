dna=input("Digite uma cadeia de DNA: ")
dna1=dna.upper()
for i in range(len(dna)):
    c=list(dna1)
    if c[i]=="A":
        dna2=dna1.replace('A', 'T')
        print(dna2)
    if c[i]=="T":
        dna2=dna1.replace('T', 'A')
        print(dna2)