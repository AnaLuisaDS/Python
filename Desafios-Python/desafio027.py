"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""

name = input('Escreva o seu nome completo:').lower().strip()
name_end = name.split()
print(f'O seu primeiro nome é {name_end[0]}.')
print(f'O seu último nome é {name_end[-1]}.')
