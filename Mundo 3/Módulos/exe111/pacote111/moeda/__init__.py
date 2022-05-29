def aumentar(p=0, aumento=0, formato=False):
    res = p + (p * aumento / 100)
    return res if formato is False else string(res)


def diminuir(p=0, diminuir=0, formato=False):
    res = p - (p * diminuir / 100)
    return res if formato is False else string(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else string(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else string(res)


def string(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(p=0, a=0, r=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:   \t{string(p)}')
    print(f'Dobro do preço:    \t{dobro(p,True)}')
    print(f'Metade do preço:   \t{metade(p,True)}')
    print(f'{a}% de aumento:   \t{aumentar(p,a,True)}')
    print(f'{r}% de redução:   \t{diminuir(p,r,True)}')
    print('-' * 30)


