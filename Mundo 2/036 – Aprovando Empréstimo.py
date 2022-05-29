valor_imovel = float(input("Valor da casa: "))
tempo = int(input("Quanto tempo para pagar ?"))
salario = float(input("Salario: "))

prestação = valor_imovel / (tempo * 12)
porcento = salario * 30 / 100
print(f'O VALOR DA PRESTAÇÃO É DE R$ {prestação:.2f}')
if prestação > porcento:
    print('O EMPRÉSTIMO FOI NEGADO!!!')
else:
    print('EMPRÉSTIMO APROVADO!')
