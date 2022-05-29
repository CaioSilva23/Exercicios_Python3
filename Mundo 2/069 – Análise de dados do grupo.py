cont_pessoas = cont_h = cont_m = 0
while True:
    print("*" * 21)
    print(' CADASTRE UMA PESSOA ')
    print("*" * 21)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()
    if idade > 18:
        cont_pessoas += 1
    if sexo in 'Mm':
        cont_h += 1
    elif sexo in 'Ff' and idade < 20:
        cont_m+=1
    resp = ' '
    while resp not in 'NS':
        resp = str(input("Quer continuar ?")).strip().upper()
    if resp == 'N':
        break
print(f'{cont_pessoas} pessoas com mais de 18 anos!')
print(f'{cont_h} homens cadastrados! ')
print(f'{cont_m} mulheres com menos de 20 anos!')
