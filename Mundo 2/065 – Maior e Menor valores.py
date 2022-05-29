resp = 'S'
cont = soma = maior = menor = media = 0
while resp in 'Ss':
    n = int(input("Digite um número: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Quer continuar ? S/N ")).strip().upper()[0]
media = soma/cont
print(f'Voce digitou {cont} e a media é {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')

























'''resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    n = int(input("Digite um número: "))
    soma += n
    cont +=1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Quer continuar ?")).upper().strip()
media = soma/cont
print(f'Voce digitou {cont} números e a media foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')

'''