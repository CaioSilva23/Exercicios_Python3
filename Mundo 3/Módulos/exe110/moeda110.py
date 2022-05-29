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


