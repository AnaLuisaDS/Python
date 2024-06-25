"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""


city = input('Escreva o nome de uma cidade').strip()
print(city[:5].lower() == 'Santo')

#Aplicação usando o operador "in"
city = input('Escreva o nome de uma cidade:').strip().upper().split()
print(f'Caso a cidade tiver "Santos" ao nome, aparecerá "True" se não "False".')
print('Santo' in city)
