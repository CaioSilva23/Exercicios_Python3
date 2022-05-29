import random
from time import sleep

print("""SUAS OPÇÃOES:
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA""")
jogador = int(input("QUAL A SUA JOGADA ?"))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print()

lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(lista)

if jogador == 1:
    jogada = 'PEDRA'
    if computador == 'TESOURA':
        print('JOGADOR VENCEU!')
    elif computador == 'PAPEL':
        print('COMPUTADOR VENCEU!')
    else:
        print('EMPATE!')
elif jogador == 2:
    jogada = 'PAPEL'
    if computador == 'TESOURA':
        print('COMPUTADOR VENCEU!')
    elif computador == 'PEDRA':
        print('JOGADOR VENCEU!')
    else:
        print('EMPATE!')
elif jogador == 3:
    jogada = 'TESOURA'
    if computador == 'PEDRA':
        print('COMPUTADOR VENCEU!')
    elif computador == 'PAPEL':
        print('JOGADOR VENCEU!')
    else:
        print('EMPATE!')


print('=' * 25)
print(f'COMPUTADOR ESCOLHEU {computador}')
print(f'JOGADOR ESCOLHEU {jogada}')
print('=' * 25)

