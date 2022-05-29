import random
from time import sleep
print('*'* 40)
print("{:^40}".format('JOGA NA MEGA SENA'))
print('*'* 40)
n = int(input("Quantos jogos voce quer que eu sorteie?"))
print(f'--------- SORTEANDO {n} JOGOS -----------')
lista = []
for i in range(n):
    sorteado = random.sample(range(60), k=6)
    sorteado.sort()
    lista.append(sorteado)
for i,jogos in enumerate (lista):
    sleep(1)
    print(f'JOGO {i+1}: {jogos}')
print('*'*5,' < BOA SORTE! >','*'*5)
