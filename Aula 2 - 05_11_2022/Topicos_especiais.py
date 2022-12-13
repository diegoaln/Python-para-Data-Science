#topicos_especiais.py

#revisão do conteudo básico especial

#Isto é um comentário de uma linha
"""
Este é um comentário
de múltiplas
linhas
"""

#tipo de variávieis
a = 30 #int
print(type(a))

x = 3.14 #float
print(type(x))

nome = 'Luiz' #str
print(type(nome))

valor = '123' #str
print(type(valor))

complexo = 3+5j #complex
print(type(complexo))

nenhum = None #NoneType
print(type(nenhum))


#Testando Tipos
import numbers

print(isinstance(a, int))
print(isinstance(x, float))

#é um número?
print(isinstance(a, numbers.Number))
print(isinstance(x, numbers.Number))

#False
print(isinstance(nome, numbers.Number))
print(isinstance(valor, numbers.Number))

print(nome.isnumeric()) #false
print(valor.isnumeric()) #true


print(isinstance(complexo, complex)) #true
print(isinstance(complexo, numbers.Number)) #true

print(isinstance(nenhum, numbers.Number)) #false


#Conversões

print('\nConversões')
a = int(3.94) #trunca
print(a)

b = float(5)
print(b)

c = 'abc'
if c.isnumeric():
    r = int(c)
else:
    r = 'Não é númerico'
print(r)

c = int('100')
print(c)


e = complex(3, 4) #3+4j
print('e:', e)

f = e.real #3.0
print(f)
