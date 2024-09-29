"""Tabuada através do Loop For"""
num = int(input('Escreva um número: '))
for n in range(1, 11):
    print(f'{num} x {n} = {num*n} ')

#Fatorial
import math
cal = int(input('Digite um valor para descobrir o seu fatorial: '))
fatc = math.factorial(cal)
print(f"{cal}! = {fatc}")
let = []

for c in range(cal, 0, -1):
    let.append(f'{c}')
print(' x '.join(let), f'= {fatc}')

for p in range(cal, 0, -1 ):
    print(f'{p}', end="")
    if p > 1:
        print(f" x ", end="")
print(f" = {fatc}")