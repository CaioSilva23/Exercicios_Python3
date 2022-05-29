pessoas = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input("Quer contiuar S/N: ")).strip().upper()
    if resp == 'N':
        break
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}kg de',end='')
for i in pessoas:
    if i[1] == maior:
        print(f' {i[0]}',end='')
print()
print(f'O menor peso foi {menor}kg de',end='')
for i in pessoas:
    if i[1] == menor:
        print(f' {i[0]}',end='')