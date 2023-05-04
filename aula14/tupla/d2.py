tabela=('Botafogo','Fortaleza','Palmeiras','Inter','Fluminense','Cruzeiro','Grêmio','São Paulo','Vasco','Atlético-MG','Santos','Red Bull Bragantino','Flamengo','Bahia','Athletico-PR','Goiás','Corinthians','Cuiabá','Coritiba','América-MG')
a=tabela[0:5]
b=tabela[-4:]
c=sorted(tabela)
d=tabela.index('Cuiabá')+1
print(f"Tabela do brasileirão: {tabela}")
print(f"{a}\n{b}\n{c}\n{d}")