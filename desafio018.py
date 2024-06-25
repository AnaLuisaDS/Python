
#Importando toda a biblioteca
import math
ang = int(input('Digite o ângulo desejado:'))
seno =  math.sin(math.radians(ang)) # - Transformar em radianos
print(f'O ângulo de {ang}° graus tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(ang))
print(f'O ângulo de {ang}° graus tem o cosseno de {seno:.2f}')
tangente = math.tan(math.radians(ang))
print('O ângulo de {}° graus tem o tangente de {:.2f}'.format(ang, tangente))


#Importando de modo específico

from math import sin,cos,tan
ang = int(input('Digite o ângulo desejado:'))
seno = sin(math.radians(ang)) # - Transformar em radianos
print(f'O ângulo de {ang} tem o seno de {seno:.2f}')
cosseno = cos(math.radians(ang))
print(f'O ângulo de {ang} tem o cosseno de {seno:.2f}')
tangente = tan(math.radians(ang))
print('O ângulo de  {} tem o tangente de {:.2f}'.format(ang, tangente))