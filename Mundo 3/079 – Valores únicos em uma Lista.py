
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar ?")).strip().upper()
    if resp == 'N':
        break
print('*'*30)
lista.sort()
print(f'Voce adicionou os valores: {lista}')