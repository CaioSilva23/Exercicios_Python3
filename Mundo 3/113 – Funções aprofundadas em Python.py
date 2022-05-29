def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário!')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'Por favor digite um número real válido!')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário!')
            return 0

        else:
            return n


inteiro = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número float: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real:.2f}  ')
