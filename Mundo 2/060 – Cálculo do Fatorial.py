n = int(input("Digite um número: "))
fat = 1
for i in range(n,0,-1):
    print(i, end='')
    print(' x ' if i > 1 else ' = ',end='')
    fat*=i
print(fat)





 # USANDO WHILE
"""n = int(input("Digite um número: "))
i = n
f = 1
while i > 0:
    print(i, end='')
    print(' x ' if i > 1 else ' = ', end='')
    f*=i
    i-=1
print(f)
"""
 # USANDO A FUNÇÃO MATH
'''import math

n = int(input("Digite um número: "))
fat = math.factorial(n)
print(f'{n}! = {fat}')'''
