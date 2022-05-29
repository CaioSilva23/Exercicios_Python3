def menu(msg):
    while True:
        try:
            print('-' * 30)
            print('        MENU PRINCIPAL   ')
            print('-' * 30)
            print("""1 - Ver pessoas cadastradas 
2 - Cadastrar nova Pessoa
3 - Sair do Sistema""")
            print('-' * 30)
            opcao = int(input(msg))
        except:
            print("ERRO! Por favor, digite um valor válido!")
        else:
            if opcao == 1:
                print('-' * 30)
                print('           OPÇÃO 1            ')
                print('-' * 30)
            elif opcao == 2:
                print('-'*30)
                print('           OPÇÃO 2            ')
                print('-' * 30)
                print()
            elif opcao == 3:
                print('Saindo do sitema... Até logo')
                break
            else:
                continue



def cadastro(nome='', idade=0):
    dicionario = {}
    dicionario['nome'] = nome
    dicionario['idade'] = idade
    return dicionario


def pessoas(dicionario=None):
    for v in dicionario.values():
        print(v, end=' ')


menu('Sua Opção: ')
