ficha = []
while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input("Quer continuar ?")).upper().strip()
    if resp == 'N':
        break
print('*' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('*' * 30)
for i, aluno in enumerate(ficha):
    print(f'{i+1:<4}{aluno[0]:<10}{aluno[2]:>8}')
print('*' * 30)
while True:
    resp = int(input("Mostrar notas de qual aluno ? (999 para parar): "))
    if resp == 999:
        break
    for i, aluno in enumerate(ficha):
        if resp == i+1:
            print(f'Notas de {aluno[0]} são {aluno[1]}')