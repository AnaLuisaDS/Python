"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu."""

import random
from time import sleep
num = random.randint(1,5)
num_end = int(input("Olá! \nEscreva um número entre 1 e 5 e descubra se eu escolhi ele também:"))
print('Analisando...')
sleep(2)
if num_end == num:
    print('PARABÉNS! Você tem uma conexão extraordinária com o algoritmo :)')
else:
    print('Opa! Foi quase, tente novamente ;P' )
    print(f'Para não ficar na dúvida o número era {num}.')
