def aumentar(p=0, aumento=0):
    res = p + (p * aumento / 100)
    return res


def diminuir(p=0, diminuir=0):
    res = p - (p * diminuir / 100)
    return res


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def string(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
