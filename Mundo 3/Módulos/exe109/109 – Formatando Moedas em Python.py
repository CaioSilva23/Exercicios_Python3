from moeda109 import string,dobro,diminuir,aumentar,metade

valor = float(input("Digite um valor: "))
print(f'O dobro de {string(valor)} é {(dobro(valor,True))}')
print(f'A metade de {string(valor)} é {(metade(valor,True))}')
print(f'O aumentando 10% de {string(valor)} temos {(aumentar(valor,10,True))}')
print(f'Reduzindo 10% de {string(valor)} temos {(diminuir(valor,10,True))}')
