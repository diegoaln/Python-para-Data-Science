#criptografia.py

#rolagem de bits

#inteiro para binário
inteiro = ord('A')      #65
binario = bin(inteiro) #0b1000001
print(binario)

#OU
binario = format(inteiro, 'b')
print(binario)


#binario para inteiro
inteiro = int(binario, 2) #base 2
print(inteiro)

#rolagem de bits para esquerda
bit1 = binario[0]
novo = binario[1:8] + bit1
print(novo)
print(binario, '=', int(binario, 2))
print(novo, '=', int(novo, 2))
