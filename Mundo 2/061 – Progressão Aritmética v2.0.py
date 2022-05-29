print('='*20)
print('{:^10}'.format('10 TERMOS DE  UMA PA'))
print('='*20)
primeiro = int(input("Primeiro termo :"))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo,end=' ')
    termo+=razao
    cont+=1
print('FIM')