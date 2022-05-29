soma = 0
cout = 0
for i in range(1,7):
    n = int(input(f"Digite o {i}° valor: "))
    if n % 2 == 0:
        soma+=n
        cout+=1
print(f'Foram digitados {cout} pares e a soma é {soma}')
