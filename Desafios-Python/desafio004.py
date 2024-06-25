""" - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele."""

box = input('Digite algo (Pode ser algum número ou letra):')

print('O tipo primitivo é da classe', type(box))
print('É um número?', box.isnumeric())
print('É uma letra?', box.isalpha())
print('É um alfanúmerico?', box.isalnum())
print('Está em maiúsculo?', box.isupper())
print('Está em minúsculo?', box.islower())
print('Contém somente espaços?', box.isspace())
print('Está capitalizada?', box.istitle())