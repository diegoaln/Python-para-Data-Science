import random


def senha():
    for x in range(10):
        num = random.randint(1, 25)
        letra = 65 + num
        print(chr(letra), end = '')


senha()


