print("*"*22)
print('  LOJA SUPER BARATÃO   ')
print("*"*22)
mais1000= total = menor = cont = 0
barato = ' '
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    cont+=1
    total +=preco
    if preco > 1000:
        mais1000+=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    mais = ' '
    while mais not in 'SN':
        mais = str(input("Quer continuar ?")).strip().upper()
    if mais == 'N':
        break
print('{:-^40}'.format("FIM DO PROGRAMA"))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')


