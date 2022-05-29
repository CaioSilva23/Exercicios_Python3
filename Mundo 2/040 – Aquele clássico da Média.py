N1 = float(input("Nota 1: "))
N2 = float(input("Nota 2: "))
media = (N1 + N2) / 2
if media < 5:
    print('ALUNO REPROVADO!')
elif media >= 7:
    print("ALUNO APROVADO!")
else:
    print('ALUNO ESTÁ DE RECUPERAÇÃO!')