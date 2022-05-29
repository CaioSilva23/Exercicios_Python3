from moeda108 import string,dobro,diminuir,aumentar,metade

valor = float(input("Digite um valor: "))
print(f'O dobro de {string(valor)} é {string(dobro(valor))}')
print(f'A metade de {string(valor)} é {string(metade(valor))}')
print(f'O aumentando 10% de {string(valor)} temos {string(aumentar(valor,10))}')
print(f'Reduzindo 10% de {string(valor)} temos {string(diminuir(valor,10))}')
