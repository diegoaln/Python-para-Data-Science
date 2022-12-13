#topicos_especiais3.py

import math

#listas com valores não númericos
lista = [-10, None, math.nan, 3.14, float('-inf'), 2, float('inf')]

print(lista) 

#for x in lista:
#    if x is not None and math.isfinite(x):
#        print(x)

for x in lista:
    #operador ternário
    print( x if x is not None and math.isfinite(x) else 'Não númerico')

#Laço de repetição While
x = 1
while x < 6:
    print(x, end = ' ') # o end tira o \n e coloca um espaço
    x += 1

#Blocos de identação
x = 0
print('\n ')
while x < 6:
    if x % 2 == 0:
        print(x, ' é par')
    else:
        print(x, 'é ímpar')
    x += 1
print('FIM')

