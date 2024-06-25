
""" Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

number = int(input('Digite um número:'))
d = number * 2
t = number * 3
r = number ** (1/2)
print('O duplo do número {}, é {}, o tríplo é {} e a raiz quadrada, é {}' .format(number, d, t, r))

#Aplicação com menos variáveis.
number = int(input('Digite um número:'))
print(f'O duplo do número {number}, é {number*2}, o tríplo é {number*3} e a raiz quadrada, é {number**(1/2)}')
