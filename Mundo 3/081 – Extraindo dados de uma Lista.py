lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar ?")).strip().upper()
    if resp == 'N':
        break
print(f'Voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
