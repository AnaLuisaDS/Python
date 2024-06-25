"""Crie um programa que leia o nome de uma pessoa e
    diga se ela tem “SILVA” no nome."""

name = input('Escreva seu nome completo:').lower()
print(f'Caso esse nome tiver "Silva" será "True", '
      f'caso contrário, será "False"\n ')
print(f'Seu nome tem Silva? {'silva' in name}')
