n = int(input("Digite um numero :"))
cont = 0
for i in range(1,n+1):
    print(i,end=' ')
    if n % i == 0:
        cont+=1
print()
print(f'O número {n} foi divisível {cont} vezes')
if cont == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')

