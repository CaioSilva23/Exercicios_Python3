import time
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número [{l}],[{c}]: "))
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]',end='')
    time.sleep(1)
    print()
