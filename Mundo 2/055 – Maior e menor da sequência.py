
lista_peso = []
for i in range(1,6):
    peso = float(input(f"Peso da {i}° pessoa: "))
    lista_peso.append(peso)

print(f'maior peso lido foi de {max(lista_peso)}kg')
print(f'menor peso lido foi de {min(lista_peso)}kg')