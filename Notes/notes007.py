frase = 'Ana Luisa Moreira dos Santos'
print(frase[2])
print(frase[:20])
print(frase[5:])
print(frase[3:16])
print(frase[1:18:2])
print(frase[::3])
print(frase.upper().count("A", 0, 28))
print(frase.capitalize().strip())
print('Ana' in frase)
print(len(frase)) #Mostrar os caracteres
print(frase.find('dos'))
print(frase.split()) #Separa com base no vázio
dividido = frase.split()
print(dividido[0])
print(dividido[1][3])


trocar = '-'
frase1 = 'Ana Luisa Moreira Dos Santos'
print(trocar.join(frase1))

delimiter = '-'
items = ['apple', 'banana', 'cherry']
result = delimiter.join(items)
print(result)

items1 = ['apple banana cherry']
print("-".join(items1))

import pygame
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input()



