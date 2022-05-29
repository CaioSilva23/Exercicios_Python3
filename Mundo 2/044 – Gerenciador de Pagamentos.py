print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input("PREÇO DAS COMPRAS: R$ "))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("QUAL A OPÇÃO DE PAGAMENTO ? "))

if opcao == 1:
    novo_preco = preco - (preco * 10/100)
elif opcao == 2:
    novo_preco = preco - (preco * 5/100)
elif opcao == 3:
    novo_preco = preco
    print(f'SUA COMPRA SERÁ PARCELADA EM 2x de R${novo_preco:.2f}')
elif opcao == 4:
    parcelas = int(input('QUANTAS PARCELAS ? '))
    novo_preco = preco + (preco * 20/100)
    print(f'SUA COMPRA SERÁ PARCELADA EM {parcelas}x de R$ {novo_preco/parcelas:.2f} COM JUROS')

else:
    novo_preco = preco
    print("OPÇÃO INVÁLIDA ! ! ! ")
print(f'SUA COMPRA DE R$ {preco:.2f} VAI CUSTAR R$ {novo_preco:.2f}')