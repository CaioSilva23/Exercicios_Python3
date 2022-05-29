from time import sleep
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
opcao = 1
while opcao != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR 
[ 3 ] MAIOR 
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR ''')
    opcao = int(input(">>> Qual é a sua opção ?"))
    if opcao == 1:
        print(f'A soma de {n1} + {n2} = {n1+n2}')
        print('*'*23)
    elif opcao == 2:
        print(f'A multiplicaçao de {n1} * {n2} = {n1*n2}')
        print('*' * 23)
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre o {n1} e {n2}, o maior é {n1}')
            print('*' * 23)
        elif n2 > n1:
            print(f'Entre o {n1} e {n2}, o maior é {n2}')
            print('*' * 23)
        else:
            print('Ambos são iguais')
            print('*' * 23)
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao > 5:
        print('Opção inválida. Tente novamente')
        print('*' * 23)
    else:
        print('Finalizando....')
        print('*' * 23)
        sleep(1)
        print('Fim do programa! Volte sempre!')



