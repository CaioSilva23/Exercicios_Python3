print('*'*15)
print('   TABUADA    ')
print("*"*15)
cont = 1

while True:
    cont = 1
    print("-" * 15)
    n = int(input("Quer ver a tabuada qual número ?"))
    print("-" * 15)
    if n < 0:
        break
    print("-" * 15)
    while cont <=10:
        print(f'{n} x {cont} = {n*cont}')
        cont +=1
print('PROGRAMA TABUADA ENCERRADO!')