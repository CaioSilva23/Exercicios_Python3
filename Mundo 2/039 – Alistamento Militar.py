from datetime import date
print('*'*14)
print('JUNTA MILITAR')
print('*'*14)
sexo = str(input("Qual o sexo ?"))
if sexo == 'M':
    ano_nascimento = int(input("Ano de nascimento: "))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 18:
        print(f'Ainda faltam {18-idade} anos para o alistamento!\nSeu alistamento será em {ano_atual+(18-idade)} ')
    elif idade == 18:
        print('Está na hora de se alistar ao serviço militar!')
    else:
        print(f"Já deveria ter se alistado há {idade-18} anos!\nSeu alistamento foi em {ano_atual-(idade-18)}")
elif sexo == 'F':
    print('MULHERES NÃO PRECISA SE ALISTAR! ')
else:
    print("OPÇÃO INVÁLIDA ! ! ! ")

