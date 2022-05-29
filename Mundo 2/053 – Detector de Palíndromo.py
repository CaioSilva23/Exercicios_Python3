frase = str(input("Digite uma frase: ")).strip().upper().replace(' ','')
invertida = frase[::-1]
print(f'O INVERSO DE {frase} É {invertida}')
if frase == invertida:
    print('A FRASE DIGITADA É UM PALÍNDROMO')
else:
    print('A FRASE DIGITADA NÃO É UM PALÍNDROMO')


