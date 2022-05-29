from random import randint
from time import sleep


def sorteio(n):
    print('Sorteando 5 valores:', end=' ')
    for i in range(5):
        num = randint(1, 10)
        n.append(num)
        print(f'{num}', end=' ')
        sleep(0.3)
    print(' FIM!')
    print('-' * 40)


def somapar(n):
    print(f'Somando os valores pares: de {n}', end='')
    soma = 0
    for i in n:
        if i % 2 == 0:
            soma += i
    print(f' Temos {soma}')
    print('-' * 40)


# GERANDO LISTA COM 5 VALORES
# = random.sample(range(10), 5)
num = []
sorteio(num)

somapar(num)
