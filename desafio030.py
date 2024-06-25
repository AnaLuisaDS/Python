""" Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

num = int(input('Escreva qualquer número:'))
resultado = num % 2
if resultado == 0:
    print('O número escolhido é par!')
else:
    print('O número escolhido é impar!')
    