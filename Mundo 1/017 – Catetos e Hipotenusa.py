co = float(input("Cateto oposto ?"))
ca = float(input('Cateto adjacente ?'))

# opcao 1  hi = math.hypot(co,ca) ... importar math
# opcao 2
hi = (co ** 2 + ca **2) ** (1/2)

print(f'A hipotenua vai medir {hi}')