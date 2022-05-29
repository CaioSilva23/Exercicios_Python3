from datetime import date
data_atual = date.today().year
cont_menor = 0
cont_maior = 0
for i in range(7):
    ano = int(input(f"Ano de nascimento da {i+1}° pessoa: "))
    idade = data_atual - ano
    if idade < 18:
        cont_menor+=1
    else:
        cont_maior+=1
print(f'Ao todo tivemos {cont_menor} pessoas menores de idade')
print(f'E também tivemos {cont_maior} pessoas maiores de idade')
