soma = 0
c = 0
for i in range(1, 501,2):
    if i % 3 == 0:
        soma += i
        c +=1
print(f'A soma de todos os {c} valores colicitados é {soma} ')