lista = [[],[]]

for i in range(7):
    n = int(input(f"Digite {i+1}° número: "))
    if n % 2 ==0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[1].sort()
lista[0].sort()
print(f'Os valores impares digitados foram {lista[1]}')
print(f'Os valores pares digitados foram {lista[0]}')