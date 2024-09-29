"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles."""
from time import sleep
import pygame
for c in range(10, 0, -1):
    print(c)
    sleep(1)
pygame.mixer.init()
pygame.mixer.music.load('music3.mp3')
pygame.mixer.music.play()
print("Aperte a tecla 'Enter' para a música parar :)")
input()
