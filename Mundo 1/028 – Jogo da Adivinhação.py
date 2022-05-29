from random import randint
computador = randint(0,5)
print('-='*25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*25)
jogador = int(input('Em que numero eu pensei ?'))
if jogador == computador:
    print('Parabéns voce conseguiu me vencer!')
else:
    print(f'GANHEI! eu pensei no numero {computador} e nao no {jogador}')
