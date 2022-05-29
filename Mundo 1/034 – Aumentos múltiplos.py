salario = float(input("Qual é o salario do funcionário ?"))
if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora')