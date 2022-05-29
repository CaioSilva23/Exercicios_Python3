from arquivo import *
from ex115.lib.interface import *

arq = 'cursoemvideo.txt'
if not aquivoExiste(arq):
    criarArquivo(arq)
while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resp == 1:
        cabeçalho('Opção 1')
        lerAquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = leiaint('Idade: ')
        cadastroPessoa(arq,nome,idade)
    elif resp == 3:
        cabeçalho('Saindo do Sistema...')
        break
    else:
        print('OPÇÃO INVÁLIDA!!!')
