#topicos_especiais2.py

#Operadores Relacionais
x = 5
y = 7
x == y
x != y
x > y
x >= y
x < y
x <= y
3 < x < 7


#Valores não númericos
import math
import numbers

x = float('nan')
print(x)
print(type(x))
print(x+1)

#não é númerico porém é instancia de number
print(isinstance(x, numbers.Number))

y = math.nan
print(math.isnan(y))

a = float('-inf')
print(a)
print(math.isinf(a)) #é infinito
print(isinstance(a, numbers.Number)) # é numerico

b = float('inf')
print(b)
print(math.isinf(b)) #é infinito
print(isinstance(b, numbers.Number)) # é numerico


print(a + b)
print(a < -1)
print(b > 1)
