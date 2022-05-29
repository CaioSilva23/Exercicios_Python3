print('=' * 20)
print('{:^10}'.format('GERADOR DE PA'))
print('=' * 20)
primeiro = int(input("Primeiro termo :"))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total+=mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    mais = int(input("\nQuantos termos quer mostrar a mais ?"))

print(f'PROGRESSÃO FINALIZADA COM {total} TERMOS MOSTRADOS! ')
