print('='*20)
print('{:^10}'.format('10 TERMOS DE  UMA PA'))
print('='*20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10-1) * razao
for i in range(termo,decimo+razao,razao):
    print(i,end=' → ')
print('ACABOU')
