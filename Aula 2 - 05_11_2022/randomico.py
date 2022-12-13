#randomico.py

import random

frutas = ['banana', 'laranja', 'kiwi', 'uva', 'abacaxi']
#embaralha
random.shuffle(frutas)
print(frutas)

#número aleatorio entre 0 e 1
print(random.random())

#retorna randomicamente 2 itens da lista
print(random.sample(frutas, k=2))

#inicio, fim (exclusivo), passo
print(random.randrange(3, 12)) #passo 1

print(random.randrange(3, 12, 3))

#igual ao randrange, porém é inclusivo
print('randint:', random.randint(3, 12))


print(chr(65), chr(66), chr(67))
print(ord('A'), ord('B'), ord('C'))


frase = 'o rato roeu a roupa'
for letra in frase:
    #print(letra, end = ' ')
    print(ord(letra), end = ' ')

#IMPORTANTE
#compreensão de lista
lista = [ord(letra) for letra in frase]
print(lista)

print('Soma (hash): ',  sum(lista))
print('Min: ',  min(lista))
print('Max: ',  max(lista))


#criptografando texto
palavra  = input('Digite um texto: ')
codigos = [ ord(c)+1 for c in palavra]
print(''.join([chr(c) for c in codigos]))

#gerador de senhas
print('Senha randomica: ',
    ''.join([chr(random.randint(97,122)) for x in range(7)]), end ='')






