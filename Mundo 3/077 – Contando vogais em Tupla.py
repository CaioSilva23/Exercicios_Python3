tupla = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS',
         'ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

for item in tupla:
    print(f'\nNa palavra {item} temos ',end='')
    for letra in item:
        if letra in 'AEIOU':
            print(letra,end=' ')
