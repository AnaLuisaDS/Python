
""" Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela seu número sucessor e seu antecessor"""

num = int(input('Digite um número:'))
ant = num - 1
suc = num + 1
print('O sucessor do número {}, é {} e o antecessor é {}' .format(num, suc, ant))

#Aplicação com menos variáveis.
num = int(input('Digite um número:'))
print(f'O sucessor do número {num}, é {num+1} e o antecessor é {num-1}')


""" Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

number = int(input('Digite um número:'))
d = number * 2
t = number * 3
r = number ** (1/2)
print('O duplo do número {}, é {}, o tríplo é {} e a raiz quadrada, é {}' .format(number, d, t, r))

#Aplicação com menos variáveis.
number = int(input('Digite um número:'))
print(f'O duplo do número {number}, é {number*2}, o tríplo é {number*3} e a raiz quadrada, é {number**(1/2)}')

""" Desafio 007 -  Faça um programa que leia as duas notas de um aluno, depois calcule 
e mostre a sua média entre as notas."""

nota1 = float(input('Digite a sua nota do primeiro bimestre:'))
nota2 = float(input('Digite a sua nota do segundo bimestre'))
media = (nota1+nota2)//2
print('Por enquanto, a sua média conforme os dados fornecidos, é de {} '.format(media))

#Aplicação com menos variáveis.
nota1 = float(input('Digite a sua nota do primeiro bimestre:'))
nota2 = float(input('Digite a sua nota do segundo bimestre'))
print(f'Por enquanto, a sua média conforme os dados fornecidos, é de {(nota1+nota2)//2}')

#Desafio 008 - Conversor de Medidas

metros = float(input('Digite quanto metros há na área desejada: '))
dm = metros * 10
cm = metros * 100
mm = metros * 1000
dam = metros / 10
hm = metros / 100
km = metros / 1000
print('De acordo com as informações fornecidas, é uma área que corresponde a {dm} decímetros, {cm} centímetros,\n'
      '{mm} milimetros, {dam} decâmetros, {hm} hectômetro e a {km} quilometros.' . format(dm, cm, mm, dam, hm, km))

#aplicação com menos variáveis

metros = float(input('Digite quanto metros há na área desejada:'))
print(f'De acordo com as informações fornecidas, é uma área que corresponde a {metros*10} decímetros, {metros*100} centímetros,\n'
      f'{metros*1000} milimetros, {metros/10} decâmetros, {metros/100 } hectômetro e a {metros/1000} quilometros.')


#desafio 9

 number = int(input('Digite um algarismo para ver sua tabuada:'))
 print('-' * 12)
 print('{} x {} = {}' .format(number, 1, number*1))
 print('{} x {} = {}' .format(number, 2, number*2))
 print('{} x {} = {}' .format(number, 3, number*3))
 print('{} x {} = {}' .format(number, 4, number*4))
 print('{} x {} = {}' .format(number, 5, number*5))
 print('{} x {} = {}' .format(number, 6, number*6))
 print('{} x {} = {}' .format(number, 7, number*7))
 print('{} x {} = {}' .format(number, 8, number*8))
 print('{} x {} = {}' .format(number, 9, number*9))
 print('{} x {} = {}' .format(number, 10, number*10))
print('-' * 12)