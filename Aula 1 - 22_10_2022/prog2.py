#prog2.py

temp = int(input('Digite a temperatura:'))

if temp < 0:
    print('Congelado')
elif temp <= 20:
    print('Frio')
elif temp <= 25:
    print('Normal')
elif temp <= 35:
    print('Quente')
else:
    print('Muito Quente')
