maior_idade = 0
acumulador = 0
cont_mulheres = 0
for i in range(1,5):
    print('{:=^20}'.format(f' {i}° PESSOA '))
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: ")).strip().upper()
    acumulador+=idade

    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome
    if sexo == 'F':
        if idade < 20:
            cont_mulheres+=1


media = acumulador/4
print(f'A media de idade do grupo é de {media} anos')
print(f'O home mais velho tem {maior_idade} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {cont_mulheres} mulheres com menos de 20 anos de idade')


