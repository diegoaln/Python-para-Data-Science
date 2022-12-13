Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5
b=6
c=a+b
c
11
a-b
-1
a*b
30
a/b
0.8333333333333334
4/3
1.3333333333333333
4//3
1
2 ** 2
4
2 ** 3
8
2 ** 4
16
2**5
32
2**6
64
2**7
128
2**8
256
import math
math.pi
3.141592653589793
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.sqrt(9)
3.0
math.pow(2,3)
8.0
5>4
True
4>5
False
5 ==5
True
5 >= 4
True
5>=5
True
4<=4
True
print('Valor de a:', a)
Valor de a: 5
print('Menor:' 4<5)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('Menor:' 4<5)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
pritn('Menor:', 4<5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    pritn('Menor:', 4<5)
NameError: name 'pritn' is not defined. Did you mean: 'print'?
print('Menor:', 4<5)
Menor: True
print('Valor de a:', a, 'Valor de b:' ,b)
Valor de a: 5 Valor de b: 6
print('Valor de a:', a, '\nValor de b:' ,b)
Valor de a: 5 
Valor de b: 6
print('Valor de a:', a, '\n\tValor de b:' ,b)
Valor de a: 5 
	Valor de b: 6
print(f'Valor de a: {a}')
Valor de a: 5
print(f'Valor de pi: {math.pi})
      
SyntaxError: unterminated string literal (detected at line 1)
print(f'Valor de pi: {math.pi}')
      
Valor de pi: 3.141592653589793
print(f'Valor de pi: {math.pi:.2}')
      
Valor de pi: 3.1
print(f'Valor de pi: {math.pi:.4}')
      
Valor de pi: 3.142
lista = ['banana', 'laranja', 'uva']
      
lista
      
['banana', 'laranja', 'uva']
type(lista)
      
<class 'list'>
print(lista[0])
      
banana
print(lista[1])
      
laranja
print(lista[2])
      
uva
len(lista)
      
3
lista.count('uva')
      
1
lista.append('kiwi')
      
lista
      
['banana', 'laranja', 'uva', 'kiwi']
lista.append('abacaxi')
      
lista
      
['banana', 'laranja', 'uva', 'kiwi', 'abacaxi']
len(lista)
      
5
lista[5]
      
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    lista[5]
IndexError: list index out of range
print(lista[4])
      
abacaxi
lista.append('uva')
      
lista.count('uva')
      
2
lista[0:5]
      
['banana', 'laranja', 'uva', 'kiwi', 'abacaxi']
lista[1:5]
      
['laranja', 'uva', 'kiwi', 'abacaxi']
lista[0:5:2]
      
['banana', 'uva', 'abacaxi']
lista
      
['banana', 'laranja', 'uva', 'kiwi', 'abacaxi', 'uva']
lista.remove('uva')
      
lista
      
['banana', 'laranja', 'kiwi', 'abacaxi', 'uva']
fruta = lista.pop()
      
fruta
      
'uva'
fruta = lista.pop()
      
fruta
      
'abacaxi'
lista
      
['banana', 'laranja', 'kiwi']
lista.append('laranja')
      
lista.append('laranja')
      
lista
      
['banana', 'laranja', 'kiwi', 'laranja', 'laranja']
lista.append('laranja')
      
lista
      
['banana', 'laranja', 'kiwi', 'laranja', 'laranja', 'laranja']
del(lista[4])
      
lista
      
['banana', 'laranja', 'kiwi', 'laranja', 'laranja']
del(lista[2])
      
lista
      
['banana', 'laranja', 'laranja', 'laranja']
lista.append('Kiwi')
      
lista
      
['banana', 'laranja', 'laranja', 'laranja', 'Kiwi']
lista = ['banana', 'laranja', 'uva', 'kiwi', 'abacate', 'acerola']
      
lista
      
['banana', 'laranja', 'uva', 'kiwi', 'abacate', 'acerola']
lista[-1]
      
'acerola'
lista[-2]
      
'abacate'
lista.sort()
      
lista
      
['abacate', 'acerola', 'banana', 'kiwi', 'laranja', 'uva']
lista.reverse()
      
lista
      
['uva', 'laranja', 'kiwi', 'banana', 'acerola', 'abacate']
copia = lista
      
copia
      
['uva', 'laranja', 'kiwi', 'banana', 'acerola', 'abacate']
lista.pop()
      
'abacate'
lista
      
['uva', 'laranja', 'kiwi', 'banana', 'acerola']
copia
      
['uva', 'laranja', 'kiwi', 'banana', 'acerola']
copia = lista.copy()
      
lista.pop()
      
'acerola'
lista
      
['uva', 'laranja', 'kiwi', 'banana']
copia
      
['uva', 'laranja', 'kiwi', 'banana', 'acerola']
lista1=[0,1,2]
      
lista2=[3,4,5]
      
lista1.append(lista2)
      
lista
      
['uva', 'laranja', 'kiwi', 'banana']
lista1
      
[0, 1, 2, [3, 4, 5]]
lista1=[0,1,2]
      
lista2=[3,4,5]
      
lista1
      
[0, 1, 2]
lista2
      
[3, 4, 5]
todos = lista1 + lista2
      
todos
      
[0, 1, 2, 3, 4, 5]
todos * 2
      
[0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
lista1.clear()
      
lista1
      
[]
lista2.clear()
      
lista2
      
[]
numeros = [0,1,2,3,4,5,6,7,8,9]
      
numero
      
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    numero
NameError: name 'numero' is not defined. Did you mean: 'numeros'?
numeros
      
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = range(10)
      
a
      
range(0, 10)
list(a)
      
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros = list(range(10))
      
numeros
      
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros = list(range(100,1001))
      
numeros
      
[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]
numeros[0]
      
100
numeros[-1]
      
1000
frutas = ['banana','laranja','uva', 'abacaxi']
      
fruta
      
'abacaxi'
frutas
      
['banana', 'laranja', 'uva', 'abacaxi']
for fruta in frutas:
      print(fruta)

      
banana
laranja
uva
abacaxi
list(range(4))
      
[0, 1, 2, 3]
for x in range(4):
      print(x)

      
0
1
2
3
for x in range(4):
      print(frutas[x])

      
banana
laranja
uva
abacaxi
for x in range(len(frutas)):
      print(frutas[x])
      ]
SyntaxError: unmatched ']'
for x in range(len(frutas)):
      print(frutas[x])

      
banana
laranja
uva
abacaxi
list(range(10,0,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for x in range(3,-1,-1):
    print(frutas[x])

    
abacaxi
uva
laranja
banana
cursos = ['pyhton', 'autocad', 'java', 'react']
'python' in cursos
False
'corte e costura' not in cursos
True
curso = input("qual curso')
              
SyntaxError: unterminated string literal (detected at line 1)
curso = input('qual curso')
              
qual curso java
curso
              
' java'
curso in cursos
              
False
cursos = ['python', 'autocad', 'java', 'react']
              
curso = input('qual curso?')
              
qual curso?java
curso in cursos
              
True
if True:
              print('tem python')
              else:
                  
SyntaxError: invalid syntax

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog1.py ===================================
Digite o curso:java
Tem o curso
dados = ['python', 'java', 'react']
dados
['python', 'java', 'react']
frutas
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    frutas
NameError: name 'frutas' is not defined
mercado = ['leite', 'pão', 'queijo', ['laranja', 'mamão', ['banana caturra', 'banana prata']]]
mercado
['leite', 'pão', 'queijo', ['laranja', 'mamão', ['banana caturra', 'banana prata']]]
mercado[0]
'leite'
mercado[1]
'pão'
mercado[2]
'queijo'
mercado[3]
['laranja', 'mamão', ['banana caturra', 'banana prata']]
mercado[3][1]
'mamão'
mercado[3][2]
['banana caturra', 'banana prata']
mercado[3][2][0]
'banana caturra'
valores = [1,2,3,4,5]
valores
[1, 2, 3, 4, 5]
for x in valores
SyntaxError: expected ':'
for x in valores:
    print( x ** 2)

    
1
4
9
16
25
#o for em cima é estrutural..... posteriormente faremos a programação funcional
valores
[1, 2, 3, 4, 5]
[x ** 2 for x in valores]
[1, 4, 9, 16, 25]
#tuplas
frutas = ('laranja', 'banana', 'uva')
frutas
('laranja', 'banana', 'uva')
frutas[0]
'laranja'
type(frutas)
<class 'tuple'>

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog2.py ===================================
Digite a temperatura:12
Traceback (most recent call last):
  File "E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog2.py", line 5, in <module>
    if temp < 0:
TypeError: '<' not supported between instances of 'str' and 'int'

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog2.py ===================================
Digite a temperatura:12

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog2.py ===================================
Digite a temperatura:-1
Congelado

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog2.py ===================================
Digite a temperatura:50
Muito Quente
valores
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    valores
NameError: name 'valores' is not defined

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog3.py ===================================
1
2
3
4
5
6
7
8
9

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog3.py ===================================
1
2
3
4

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog3.py ===================================
1
2
3
4
6
7
8
9
10

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog3.py ===================================
1
2
3
4
6
7

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog3.py ===================================
1
2
3
4
6
7
for c in range(65,91):
              print(c)

              
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
for c in range(65,91):
              print(chr(c))

              
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
for c in range(65,91):
              print(chr(c), end='')

              
ABCDEFGHIJKLMNOPQRSTUVWXYZ
for c in range(65,91):
              print(chr(c), end='', ', ')
              
SyntaxError: positional argument follows keyword argument
for c in range(65,91):
              print(chr(c), end=' ')

              
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
import time
for c in range(65,91):
              print(chr(c), end=' ')
              time.sleep(0.1)

              
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
import random
random.random()
0.7764873164833034
random.random()
0.24266603772398687
random.randint(1,26)
8
random.randint(1,26)
11
random.randint(1,26)
19
random.randint(1,26)
1
random.randint(1,26)
23
random.randint(1,26)
18
random.randint(1,26)
10
random.randint(1,26)
21
num = random.randint(0,26)
letra = 65 + num
chr(letra)
'F'
for x in range(10):
    num = random.ranint(1, 25)
    letra = 65 + num
    print(chr(letra), end = '')

    
Traceback (most recent call last):
  File "<pyshell#217>", line 2, in <module>
    num = random.ranint(1, 25)
AttributeError: module 'random' has no attribute 'ranint'. Did you mean: 'randint'?
for x in range(10):
    num = random.randint(1, 25)
    letra = 65 + num
    print(chr(letra), end = '')

    
JUZSNTUQCV

for x in range(10):
    num = random.randint(1, 25)
    letra = 97 + num
    print(chr(letra), end = '')

    
cfbssrrgid

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog4.py ===================================
HCINVULFHGgrrsrxshgj

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog4.py ===================================

x
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    x
NameError: name 'x' is not defined
senha
<function senha at 0x000001A0CEE92B00>

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog4.py ===================================
JXGRNTHZDT

for angulo in range(0, 360, 90):
    print(angulo)

    
0
90
180
270

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog5.py ===================================

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog5.py ===================================

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog5.py ===================================

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog5.py ===================================
Traceback (most recent call last):
  File "E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog5.py", line 12, in <module>
    turtle.left(100)
  File "<string>", line 8, in left
  File "C:\Users\diegoa01\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 1700, in left
    self._rotate(angle)
  File "C:\Users\diegoa01\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 3278, in _rotate
    self._update()
  File "C:\Users\diegoa01\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\diegoa01\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\diegoa01\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog5.py ===================================

=================================== RESTART: E:/OneDrive - Castrolanda - Cooperativa Agroindustrial Ltda/Treinamentos/Data Science com Python/prog5.py ===================================
