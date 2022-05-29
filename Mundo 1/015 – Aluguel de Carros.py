dias = int(input("Quantos dias o carro foi alugado ?"))
km = float(input('Km percorrido ? '))

valor = (60 * dias) + (0.15 * km)
print(f'O total a pagar é de R${valor:.2f}')