"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""
s1 = float(input('Escreva o primeiro segmento:'))
s2 = float(input('Escreva o segundo segmento:'))
s3 = float(input('Escreva o terceiro segmento:'))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print(f'Os segmentos fornecidos \033[4:32m PODEM \033[m formar um triângulo')
else:
    print(f'Os segmentos fornecidos \033[4:31m NÃO PODEM \033[m formar um triângulo.')
