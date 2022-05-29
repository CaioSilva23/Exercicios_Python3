def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param n: uma ou mais notas do aluno
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionário com várias informações sobre a situação do aluno
    """
    dicionario = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if dicionario['media'] <= 5:
            dicionario['situação'] = 'Recuperação'
        elif dicionario['media'] <= 7:
            dicionario['situação'] = 'Bom'
        else:
            dicionario['situação'] = 'Muito bom'

    return dicionario


print(notas(5, 5, 5,sit=True))
