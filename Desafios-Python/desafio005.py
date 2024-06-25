
""" Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela seu número sucessor e seu antecessor"""

num = int(input('Digite um número:'))
ant = num - 1
suc = num + 1
print('O sucessor do número {}, é {} e o antecessor é {}' .format(num, suc, ant))

#Aplicação com menos variáveis.
num = int(input('Digite um número:'))
print(f'O sucessor do número {num}, é {num+1} e o antecessor é {num-1}')




