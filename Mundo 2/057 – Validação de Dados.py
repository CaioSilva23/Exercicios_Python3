sexo = str(input("Informe seu sexo: ")).strip().upper()
while 'F' != sexo != 'M':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
if sexo == 'M':
    print(f'Sexo masculino registrado com sucesso!')
else:
    print(f'Sexo feminino registrado com sucesso!')