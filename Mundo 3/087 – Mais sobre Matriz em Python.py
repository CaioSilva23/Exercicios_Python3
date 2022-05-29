matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = soma_terceira_coluna = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite o valor [{l}],[{c}]: "))
        if matriz[l][c] % 2 ==0:
            soma+= matriz[l][c]
print('*'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('*'*30)

print(f'A soma dos pares é {soma}')
for l in range(0,3):
    soma_terceira_coluna+= matriz[l][2]
print(f'A soma da terceira coluna é {soma_terceira_coluna}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}')

