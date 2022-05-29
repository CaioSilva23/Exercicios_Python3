lista = []
for i in range(3):
    valor = int(input(f'Digite o {i+1}° valor: '))
    lista.append(valor)
print(f'O maior valor digitado foi {max(lista)}!')
print(f'O menor valor digitado  foi {min(lista)}!')