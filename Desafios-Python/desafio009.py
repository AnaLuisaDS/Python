""" - Faça um programa que leia um número inteiro e mostre sua tabuada"""

number = int(input('Digite um algarismo para ver sua tabuada:'))

print('-' * 12)

print('{} x {:2} = {}' .format(number, 1, number*1))
print('{} x {:2} = {}' .format(number, 2, number*2))
print('{} x {:2} = {}' .format(number, 3, number*3))
print('{} x {:2} = {}' .format(number, 4, number*4))
print('{} x {:2} = {}' .format(number, 5, number*5))
print('{} x {:2} = {}' .format(number, 6, number*6))
print('{} x {:2} = {}' .format(number, 7, number*7))
print('{} x {:2} = {}' .format(number, 8, number*8))
print('{} x {:2} = {}' .format(number, 9, number*9))
print('{} x {:2} = {}' .format(number, 10, number*10))
#O uso de {:2} no código garante que os números estejam alinhados corretamente
print('-' * 12)