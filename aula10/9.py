primeira=input("Digite algo: ")
segunda=input("Digite mais alguma coisa: ")
terceira=""

for i in primeira:
    if i not in segunda:
        terceira+=i
print(f"1ª String: {primeira}")
print(f"2ª String: {segunda}")
print(f"3ª String: {terceira}")