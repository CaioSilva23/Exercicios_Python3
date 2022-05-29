def helpp(n):
    return help(n)


while True:
    comando = str(input("Digite um comando: ")).strip()
    help(comando)
    if comando == 'parar':
        break
