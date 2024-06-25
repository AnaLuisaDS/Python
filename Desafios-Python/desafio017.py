#Importando toda a biblioteca

import math
cp = float(input('Escreva o comprimento do cateto oposto:'))
cdj = float(input('Escreva o comprimento do cateto adjacente:'))
h = math.hypot(cp, cdj)
print(f'A hipotenusa medirá {h :.2f}.')

#Importando especifícamente

from math import hypot

cp = float(input('Escreva o comprimento do cateto oposto: '))
cdj = float(input('Escreva o comprimento do cateto adjacente: '))
h = hypot(cp, cdj)
print(f'A hipotenusa medirá {h :.2f}.')

#Sem utilizar a biblioteca
cp = float(input('Escreva o comprimento do cateto oposto:'))
cdj = float(input('Escreva o comprimento do cateto adjacente:'))
h = (cp ** 2 + cdj ** 2) ** 1/2
print(f'A hipotenusa medirá {h:.2f}.')
