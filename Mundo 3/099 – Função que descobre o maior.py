from time import sleep
def maior(*num):
    maior = 0
    for i,m in enumerate(num):
        if i == 0:
            maior = m
        elif m > maior:
            maior = m
    print('Analisando os valores passados...',end='')
    for v in num:
        print(v,end=' ')
    print()
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print('-'*38)
maior(1,2,3,60)
sleep(1)
maior(3,4,5,67,2)
maior()

'''
def maior(*num):
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi {max(num)}')
maior(1,2,3,4,5,6,87)
'''