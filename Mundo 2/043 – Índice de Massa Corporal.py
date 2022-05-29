peso = float(input("QUAL PESO ? "))
altura = float(input("QUAL A ALTURA ?"))

IMC = peso / (altura ** 2)
print(f"SEU IMC É DE {IMC:.1f}")
if IMC < 18.5:
    print("ABAIXO DO PESO!")
elif 18.5 <= IMC <= 24.9:
    print('PESO NORMAL!')
elif IMC <= 29.9:
    print('SOBREPESO!')
elif IMC <= 39.9:
    print('OBESIDADE!')
else:
    print('OBESIDADE GRAVE!')
