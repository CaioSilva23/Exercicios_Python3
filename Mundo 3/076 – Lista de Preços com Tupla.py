tupla = (('Lápis',1.75), ('Borracha',2.00),('Caderno',15.90),
         ('Estojo',25.00),('Compasso',9.99),('Mochila',120.32),
         ('Canetas',22.30),('Livro',34.90))
print('='*40)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('='*40)
for produto, preco in tupla:
    print(f'{produto:.<30} R$ {preco:.2f}')
print('='*40)
