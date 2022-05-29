import math

angulo = float(input('Angulo: '))
seno = math.sin(math.radians(angulo))
print(f'Angulo de {angulo} tem o SENO de {seno:.2f}')

cosseno = math.cos(math.radians(angulo))
print(f'Angulo de {angulo} tem o COSSENO de {cosseno:.2f}')

tangente = math.tan(math.radians(angulo))
print(f'Angulo de {angulo} tem a TANGENTE de {tangente:.2f}')
