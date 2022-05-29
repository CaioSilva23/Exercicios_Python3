from random import randint
computador = randint(0,10)
print('-='*25)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-='*25)

palpite = int(input('Qual é o seu palpite ?'))
tentativas = 1
while computador != palpite:
    if palpite > computador:
        print('Menos... tente outra vez.')
        palpite = int(input('Qual é o seu palpite ?'))
    elif palpite < computador:
        print('Mais... tente outra vez.')
        palpite = int(input('Qual é o seu palpite ?'))
    tentativas+=1

print(f'Acertouuu com {tentativas} tentativas. Parabéns!')
