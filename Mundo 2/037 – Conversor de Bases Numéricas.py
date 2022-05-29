n = int(input("DIGITE UM NUMERO INTEIRO: "))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL 
[ 3 ] CONVERTER PARA HEXADECIMAL''')

opcao = int(input("QUAL OPÇÃO ?"))

if opcao == 1:
    print(f'{n} convetido para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print("OPÇÃO INVÁLIDA ! ! ! ")
