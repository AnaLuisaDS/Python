"""Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados."""


#Aplicação através do replace
num = input('Escreva algum número de 4 algarismos. Ex = 9999:').strip()
num_end = num.replace('',' ').split()
print(f'A unidade do {num} é: {num_end[3]}\n'
      f'A dezena do {num} é: {num_end[2]}\n'
      f'A centena do {num} é: {num_end[1]}\n'
      f'O milhar do {num} é: {num_end[0]}')


#Aplicação através do join
num = input('Escreva algum número de 0 a 9999:').strip().split()
numend = " ".join(num)
print(f'A unidade do {num} é: {numend[3]}\n'
      f'A dezena do {num} é: {numend[2]}\n'
      f'A centena do {num} é: {numend[1]}\n'
      f'O milhar do {num} é: {numend[0]}')


#Aplicação através do int
num = int(input('Escreva algum número de 0 a 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade {num} é: {u}\n'
      f'A dezena {num} é: {d}\n'
      f'A centena do {num} é: {c}\n'
      f'O milhar do {num} é: {m}\n')