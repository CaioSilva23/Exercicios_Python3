from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for i in n:
    print(i,end=' ')

print(f'\nMaior valor: {max(n)}')
print(f'Menor valor: {min(n)}')


'''
import random

n1 = (random.sample(range(1,20),6))

print('jogo: ',n1)
print(max(n1))
print(min(n1))
'''