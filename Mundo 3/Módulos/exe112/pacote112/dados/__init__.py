def leiadin(msg):
    ok = False
    while not ok:
        n = str(input(msg)).strip().replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'ERRO! "{n}" não é um preço válido!')
        else:
            return float(n)

