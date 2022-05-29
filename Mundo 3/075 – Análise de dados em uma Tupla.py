n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite o terceiro número: ')),
     int(input('Digite o quarto número: ')))

print(f'Voce digitou os valores {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3)+1}')
else:
    print('O valor 3 nao apareceu em nenhuma posição')
print('Os valores pares são ', end='')
for i in n:
    if i % 2 == 0:
        print(i,end=' ')



'''lista = []
for i in range(4):
    n = int(input("Valor: "))
    lista.append(n)

tupla = tuple(lista)
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

for i, n in enumerate(tupla):
    if n == 3:
        print(f'O valor 3 apareceu na posição {i+1}°')
print('Os valores pares digitados foram: ',end='')
for n in tupla:
    if n % 2 == 0:
        print(n,end= ' ')
'''


