velocidade = float(input('Qual é a velocidade do carro ?'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Voce excedeu o limite permitido que é 80Km/h')
    print(f'Voce deve pagar um multa de R$ {multa}')
print('Tenha um ótimo dia! Dirija com segurança!')