from datetime import date

nascimento = int(input("ANO DE NASCIMENTO: "))
idade = date.today().year - nascimento

print(f'O ATLETA TEM {idade} ANOS!')
if idade <= 9:
    print("ATLETA MIRIM")
elif idade <= 14:
    print('ATLETA INFANTIL')
elif idade <= 19:
    print('ATLETA JUNIOR')
elif idade <= 25:
    print('ATLETA SÊNIOR')
else:
    print('ATLETA MASTER')

