from ex115.lib.interface import *


def aquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do ex115!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o ex115!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for p in a:
            dado = p.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastroPessoa(arq, n='desconhecido', i=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do aquivo!')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('Erro ao escrever os dados!')
        else:
            print(f'Novo resgistro de {n} adicionado')
            a.close()
