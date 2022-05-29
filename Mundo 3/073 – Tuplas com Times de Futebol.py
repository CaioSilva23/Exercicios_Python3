tupla = ('Corinthians','Bragantino','Atlético - MG','Coritiba','São Paulo',
         'Santos','Cuiabá','Internacional','Avaí','América - MG','Palmeiras',
         'Flamengo','Botafogo','Fluminense','Ceará','Athletico - PR','Atlético - GO',
         'Goiás','Juventude','Fortaleza')
print('*'*30)
print(f'Tabela do Brasileirão 2021: {tupla}')
print('*'*30)
print(f'Os 5 primeiros colocados são: {tupla[:5]}')
print('*'*30)
print(f'Os 5 últimos colocados são: {tupla[-5:]}')
print('*'*30)
print(f'Times em ordem alfabética: {sorted(tupla)}')
print('*'*30)
print(f'O Flamengo está na {tupla.index("Flamengo")+1}°')
'''
for i, time in enumerate(tupla):
    if time == "Flamengo":
        print(f'{time} está na posição {i+1}°')
'''
