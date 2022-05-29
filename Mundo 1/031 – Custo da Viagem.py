km = float(input('Qual a distancia da viagem em km/h ?'))
preco = km * 0.50 if km <= 200 else km * 0.45
print(f'Valor total da passagem é R$ {preco}')