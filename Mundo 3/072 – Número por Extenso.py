tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

while True:
    n = int(input("Digite um número de 0 a 10: "))
    if 0 <= n <= 10:
        print(f'Voce digitou o número {tupla[n]}')

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar ?")).strip().upper()
    if resp == 'N':
        break