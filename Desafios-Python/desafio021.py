
import pygame
pygame.init()
pygame.mixer.music.load('music1.mp3')
pygame.mixer.music.play()
print('Caso queira parar, aperte qualquer tecla! :)')
input( )

#Importando de modo específico
from pygame import mixer
mixer.init()
mixer.music.load('music1.mp3')
mixer.music.play()
print('Caso queira parar, aperte qualquer tecla! :)')
input( )
