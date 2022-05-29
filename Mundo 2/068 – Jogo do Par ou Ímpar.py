from random import randint
print("*"*25)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("*"*25)
cont = 0
while True:
    pc = randint(1,10)
    eu = int(input("Digite um valor ?"))
    soma = pc + eu
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Ímpar ? [P/I]')).strip().upper()[0]

    print(f'Voce jogou {eu} e o pc jogou {pc}. O resultado é {soma}', end='')
    print(f'DEU PAR' if soma % 2 == 0 else ' DEU ÍMPAR')
    if parouimpar == 'I':
        if soma % 2 == 0:
            print('Voce perdeu! ')
            break
        else:
            print('Voceu ganhou!')
            cont+=1

    elif parouimpar == 'P':
        if soma % 2 ==0:
            print('Voce ganhou!')
            cont+=1
        else:
            print('Voce perdeu!')
            break
print(f'GAMER OVER! Voce venceu {cont} vezes.')